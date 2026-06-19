#!/usr/bin/env python3
"""
JF Web Studios — Lead Scout via Google Places API
Finds businesses with NO website in Houston area.
Saves results to JSON for Jarvis to log to Leads entity.

Usage: python3 lead_scout_places.py [industry] [city]
Example: python3 lead_scout_places.py "barbershop" "Houston TX"

Requires: GOOGLE_PLACES_API_KEY in environment
"""

import os
import sys
import json
import time
import googlemaps

API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY", "")

INDUSTRIES = [
    ("barbershop", "Barbershop"),
    ("nail salon", "Nail Salon"),
    ("hvac", "HVAC"),
    ("landscaping", "Landscaping"),
    ("auto body shop", "Auto Shop"),
    ("cleaning service", "Cleaning"),
    ("electrician", "Electrician"),
    ("plumber", "Plumber"),
    ("restaurant", "Restaurant"),
    ("general contractor", "Contractor"),
]

CITIES = [
    ("Houston", "TX", 29.7604, -95.3698),
    ("Katy", "TX", 29.7858, -95.8245),
    ("Pearland", "TX", 29.5635, -95.2860),
    ("Sugar Land", "TX", 29.6196, -95.6349),
    ("Pasadena", "TX", 29.6910, -95.2091),
    ("Humble", "TX", 29.9988, -95.2622),
]

def find_leads(api_key, industry_query, industry_label, city_name, state, lat, lng):
    gmaps = googlemaps.Client(key=api_key)
    leads = []
    
    # Search within 15km radius of city center
    results = gmaps.places_nearby(
        location=(lat, lng),
        radius=15000,
        keyword=industry_query,
        language="en"
    )
    
    places = results.get("results", [])
    
    # Get next page if available
    next_token = results.get("next_page_token")
    if next_token:
        time.sleep(2)
        results2 = gmaps.places_nearby(page_token=next_token)
        places += results2.get("results", [])
    
    for place in places:
        place_id = place.get("place_id")
        name = place.get("name", "")
        rating = place.get("rating", 0)
        review_count = place.get("user_ratings_total", 0)
        vicinity = place.get("vicinity", "")
        
        # Get full details to check for website
        try:
            details = gmaps.place(
                place_id=place_id,
                fields=["name", "formatted_address", "formatted_phone_number", 
                        "website", "url", "rating", "user_ratings_total", "business_status"]
            )
            detail = details.get("result", {})
            
            website = detail.get("website", "")
            status = detail.get("business_status", "OPERATIONAL")
            phone = detail.get("formatted_phone_number", "")
            address = detail.get("formatted_address", vicinity)
            maps_url = detail.get("url", "")
            
            # Only include OPERATIONAL businesses with NO website
            if status == "OPERATIONAL" and not website:
                lead = {
                    "business_name": name,
                    "industry": industry_label,
                    "phone": phone,
                    "address": address,
                    "city": city_name,
                    "state": state,
                    "has_website": False,
                    "website_url": "",
                    "google_maps_url": maps_url,
                    "rating": rating,
                    "review_count": review_count,
                    "status": "New",
                    "source": "Google Maps Scout"
                }
                leads.append(lead)
                print(f"  ✅ NO WEBSITE: {name} | {phone} | Rating: {rating}")
            else:
                print(f"  ⬜ Has website: {name}")
                
        except Exception as e:
            print(f"  ⚠️  Error getting details for {name}: {e}")
        
        time.sleep(0.1)  # Rate limit
    
    return leads

def main():
    if not API_KEY:
        print("❌ GOOGLE_PLACES_API_KEY not set")
        sys.exit(1)
    
    target_industry = sys.argv[1] if len(sys.argv) > 1 else "barbershop"
    target_city = sys.argv[2] if len(sys.argv) > 2 else "Houston"
    
    all_leads = []
    
    for industry_query, industry_label in INDUSTRIES:
        if target_industry.lower() not in industry_query.lower() and target_industry.lower() != "all":
            continue
            
        for city_name, state, lat, lng in CITIES:
            if target_city.lower() not in city_name.lower() and target_city.lower() != "all":
                continue
                
            print(f"\n🔍 Scanning: {industry_label} in {city_name}, {state}")
            leads = find_leads(API_KEY, industry_query, industry_label, city_name, state, lat, lng)
            all_leads.extend(leads)
            print(f"   Found {len(leads)} leads without websites")
    
    # Output results
    output_file = "/tmp/leads_found.json"
    with open(output_file, "w") as f:
        json.dump(all_leads, f, indent=2)
    
    print(f"\n🎯 Total leads found: {len(all_leads)}")
    print(f"📄 Saved to: {output_file}")
    return all_leads

if __name__ == "__main__":
    main()
