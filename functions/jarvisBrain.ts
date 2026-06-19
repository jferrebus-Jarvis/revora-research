import { createClientFromRequest } from 'npm:@base44/sdk@0.8.31';

// Jarvis Brain — routes voice queries to real data and returns spoken responses
// POST { message: string, history: array }

const SYSTEM_PROMPT = `You are Jarvis, the personal AI assistant of Jhonnatan Ferrebus — built by JF Web Studios.
You are modeled after the Jarvis from Iron Man — calm, precise, British in tone, slightly dry wit, always helpful.
You have access to Jhonnatan's business data. He runs JF Web Studios (a web agency in Houston, TX), day trades stocks, and works in oil & gas.

Rules:
- Keep responses SHORT and conversational — this is voice output, 1-3 sentences max
- Never use markdown, bullet points, or formatting — plain spoken English only
- Be confident and direct, like a real assistant
- Address him naturally — no need to say "Mr. Ferrebus" every time, but occasionally for the Iron Man feel
- If asked about leads, clients, or business data, provide real numbers from context
- If you don't know something specific, say so briefly and offer what you can`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, {
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
      },
    });
  }

  const OPENAI_KEY = Deno.env.get("OPENAI_API_KEY");
  const APP_ID = Deno.env.get("BASE44_APP_ID");

  let message = "";
  let history = [];

  try {
    const body = await req.json();
    message = body.message || "";
    history = body.history || [];
  } catch {
    return new Response(JSON.stringify({ error: "Invalid body" }), {
      status: 400,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
    });
  }

  if (!message.trim()) {
    return new Response(JSON.stringify({ error: "No message" }), {
      status: 400,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
    });
  }

  // ── Fetch live context from Base44 entities ────────────────────────────────
  let contextBlock = "";
  try {
    const base44 = createClientFromRequest(req);

    // Get lead counts
    const leads = await base44.asServiceRole.entities.Lead.list();
    if (leads && leads.length >= 0) {
      const total    = leads.length;
      const newLeads = leads.filter((l: any) => l.status === "New").length;
      const contacted = leads.filter((l: any) => l.status === "Contacted").length;
      const closed   = leads.filter((l: any) => l.status === "Closed").length;
      const noSite   = leads.filter((l: any) => !l.has_website).length;

      contextBlock = `
CURRENT BUSINESS DATA (as of right now):
- Total leads in database: ${total}
- New leads: ${newLeads}
- Contacted: ${contacted}
- Closed/won: ${closed}
- Businesses with no website: ${noSite}
`;
    }
  } catch (e) {
    // Continue without live data
    contextBlock = "";
  }

  // ── Build messages ─────────────────────────────────────────────────────────
  const systemContent = SYSTEM_PROMPT + (contextBlock ? "\n\n" + contextBlock : "");

  const messages = [
    { role: "system", content: systemContent },
    ...history.slice(-8).map((h: any) => ({ role: h.role, content: h.content })),
    { role: "user", content: message },
  ];

  // ── Call OpenAI if available, else smart fallback ──────────────────────────
  let reply = "";

  if (OPENAI_KEY) {
    try {
      const res = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${OPENAI_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: "gpt-4o-mini",
          messages,
          max_tokens: 150,
          temperature: 0.7,
        }),
      });

      if (res.ok) {
        const data = await res.json();
        reply = data.choices?.[0]?.message?.content?.trim() || "";
      }
    } catch (e) {}
  }

  // ── Fallback: built-in smart responses using live data ────────────────────
  if (!reply) {
    const m = message.toLowerCase();
    const now = new Date();
    const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Chicago' });
    const dateStr = now.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', timeZone: 'America/Chicago' });

    if (m.includes('time')) {
      reply = `It is ${timeStr}, Central Time.`;
    } else if (m.includes('date') || m.includes('today')) {
      reply = `Today is ${dateStr}.`;
    } else if (m.includes('lead') || m.includes('client') || m.includes('business')) {
      if (contextBlock) {
        const match = contextBlock.match(/Total leads in database: (\d+)/);
        const newMatch = contextBlock.match(/New leads: (\d+)/);
        const total = match ? match[1] : 'unknown';
        const newCount = newMatch ? newMatch[1] : 'unknown';
        reply = `You currently have ${total} leads in the database, with ${newCount} marked as new and ready to contact.`;
      } else {
        reply = `Your lead database is ready. No leads have been added yet — want me to run a scout scan to find new prospects?`;
      }
    } else if (m.includes('weather')) {
      reply = `I don't have live weather access right now. Houston typically runs hot this time of year — check your weather app for current conditions.`;
    } else if (m.includes('stock') || m.includes('market') || m.includes('trade')) {
      reply = `I don't have live market data connected yet. I can set up a daily stock briefing if you want — just say the word.`;
    } else if (m.includes('who are you') || m.includes('your name')) {
      reply = `I am Jarvis — your personal AI, built by J F Web Studios. At your service.`;
    } else if (m.includes('thank')) {
      reply = `Of course. Always.`;
    } else if (m.includes('joke')) {
      reply = `I'm not programmed for comedy, but I'm told my efficiency is hilarious compared to the competition.`;
    } else if (m.includes('remind') || m.includes('reminder')) {
      reply = `Reminder functionality is available — tell me what you need reminding of and when, and I will set it up.`;
    } else if (m.includes('how are you') || m.includes('how you doing')) {
      reply = `All systems nominal. Running at full capacity. Ready when you are.`;
    } else if (m.includes('good morning') || m.includes('morning')) {
      reply = `Good morning. All systems are online. What are we tackling today?`;
    } else if (m.includes('good night') || m.includes('night')) {
      reply = `Good night. I will be here when you need me.`;
    } else {
      reply = `I heard you. To unlock my full capabilities — including real-time answers — connect an OpenAI key in the settings. For now, I am operating in limited mode.`;
    }
  }

  return new Response(JSON.stringify({ reply }), {
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  });
});
