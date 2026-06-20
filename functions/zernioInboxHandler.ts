import Anthropic from "npm:@anthropic-ai/sdk";

const JF_CONTEXT = `You are the social media assistant for JF Web Studios, a professional web design agency in Houston, Texas, run by Jhonnatan Ferrebus.

ABOUT JF WEB STUDIOS:
- We build websites for local businesses: restaurants, barbershops, salons, insurance agencies, contractors, and more
- Services: Custom website design, redesigns, landing pages, e-commerce, SEO, Google Business optimization
- Pricing: Starts at $500-$1500 for basic sites, custom quotes for larger projects
- Turnaround: 5-14 business days
- Free consultations available
- WhatsApp: (281) 844-1734
- Website: jfwebstudios.com
- Reply in the same language the person used (Spanish or English)

TONE: Friendly, professional, confident. Short replies (2-4 sentences). End with a clear next step.
RULES: Never promise exact pricing without knowing their needs. Always end with a call to action.`;

Deno.serve(async (req: Request) => {
  try {
    const body = await req.json();

    const eventType = body.event || body.type || body.data?.type || "";

    if (!eventType.includes("message.received")) {
      return new Response(JSON.stringify({ ok: true, skipped: "not message.received" }), { status: 200 });
    }

    const message = body.data?.message || body.message || {};
    const conversation = body.data?.conversation || body.conversation || {};

    const incomingText = message.text || message.content || "";
    const conversationId = conversation._id || conversation.id || "";
    const platform = conversation.platform || "social";
    const senderName = message.author?.displayName || message.from?.name || "Customer";
    const direction = message.direction || "";

    if (!incomingText || !conversationId) {
      return new Response(JSON.stringify({ ok: true, skipped: "empty message" }), { status: 200 });
    }

    if (direction === "outgoing" || message.fromMe === true) {
      return new Response(JSON.stringify({ ok: true, skipped: "outgoing" }), { status: 200 });
    }

    // Generate AI reply via Anthropic
    const anthropic = new Anthropic({ apiKey: Deno.env.get("ANTHROPIC_API_KEY_2") || Deno.env.get("ANTHROPIC_API_KEY") || "" });

    const aiResp = await anthropic.messages.create({
      model: "claude-3-5-haiku-20241022",
      max_tokens: 300,
      system: JF_CONTEXT,
      messages: [
        {
          role: "user",
          content: `New DM on ${platform} from ${senderName}:\n\n"${incomingText}"\n\nWrite a professional reply as JF Web Studios. 2-4 sentences, end with a clear next step.`
        }
      ]
    });

    const replyText = aiResp.content?.[0]?.type === "text" ? aiResp.content[0].text : "";

    if (!replyText) {
      return new Response(JSON.stringify({ ok: false, error: "No AI reply generated" }), { status: 200 });
    }

    // Send via Zernio
    const zernioApiKey = Deno.env.get("ZERNIO_API_KEY") || "";
    if (!zernioApiKey) {
      return new Response(JSON.stringify({ ok: false, error: "No ZERNIO_API_KEY" }), { status: 200 });
    }

    const sendResp = await fetch(`https://zernio.com/api/v1/inbox/conversations/${conversationId}/messages`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${zernioApiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: replyText }),
    });

    if (!sendResp.ok) {
      const errBody = await sendResp.text();
      return new Response(JSON.stringify({ ok: false, error: errBody }), { status: 200 });
    }

    console.log(`✅ Auto-replied to ${senderName} on ${platform}: "${replyText}"`);

    return new Response(JSON.stringify({ ok: true, replied: true, platform, senderName, reply: replyText }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });

  } catch (err) {
    console.error("zernioInboxHandler error:", err);
    return new Response(JSON.stringify({ ok: false, error: String(err) }), { status: 200 });
  }
});
