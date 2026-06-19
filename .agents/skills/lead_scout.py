#!/usr/bin/env python3
"""
JF Web Studios — Lead Scout
Searches Google Maps for businesses without websites in Houston area.
Industries: Barbershops, Restaurants, HVAC, Nail Salons, Landscapers,
            Contractors, Auto Shops, Cleaning, Plumbers, Electricians
"""

import json
import time
import sys

INDUSTRIES = [
    ("barbershop", "Barbershop"),
    ("nail salon", "Nail Salon"),
    ("hvac contractor", "HVAC"),
    ("landscaping company", "Landscaping"),
    ("auto body shop", "Auto Shop"),
    ("cleaning service", "Cleaning"),
    ("electrician", "Electrician"),
    ("plumber", "Plumber"),
    ("restaurant", "Restaurant"),
    ("general contractor", "Contractor"),
]

CITIES = [
    "Houston TX",
    "Katy TX",
    "Pearland TX",
    "Sugar Land TX",
    "Pasadena TX",
    "Humble TX",
    "Baytown TX",
    "Conroe TX",
]

def build_search_url(industry, city):
    query = f"{industry} in {city}".replace(" ", "+")
    return f"https://www.google.com/maps/search/{query}"

if __name__ == "__main__":
    # Print search targets
    targets = []
    for industry_query, industry_label in INDUSTRIES:
        for city in CITIES[:3]:  # Start with top 3 cities
            targets.append({
                "url": build_search_url(industry_query, city),
                "industry": industry_label,
                "city": city
            })
    print(json.dumps(targets, indent=2))
    print(f"\nTotal search targets: {len(targets)}")
