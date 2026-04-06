#!/usr/bin/env python3
"""
Generate city data for appliance repair pages.
Uses realistic cost data for diagnostics, common repairs, emergency calls, and premium appliances.
"""
import json
from pathlib import Path

CITIES = [
    {"city": "Fort Worth", "state": "Texas", "stateAbbr": "TX", "slug": "fort-worth-tx", "population": 935508, "climate": "hot-humid", "season": "Year-round emergency demand"},
    {"city": "Dallas", "state": "Texas", "stateAbbr": "TX", "slug": "dallas-tx", "population": 1304379, "climate": "hot-humid", "season": "Year-round emergency demand"},
    {"city": "Houston", "state": "Texas", "stateAbbr": "TX", "slug": "houston-tx", "population": 2304580, "climate": "hot-humid", "season": "Year-round emergency demand"},
    {"city": "Austin", "state": "Texas", "stateAbbr": "TX", "slug": "austin-tx", "population": 978908, "climate": "hot-dry", "season": "Year-round repair demand"},
    {"city": "San Antonio", "state": "Texas", "stateAbbr": "TX", "slug": "san-antonio-tx", "population": 1434625, "climate": "hot-dry", "season": "Year-round repair demand"},
    {"city": "Phoenix", "state": "Arizona", "stateAbbr": "AZ", "slug": "phoenix-az", "population": 1608139, "climate": "desert", "season": "Summer AC-adjacent appliance failures"},
    {"city": "Scottsdale", "state": "Arizona", "stateAbbr": "AZ", "slug": "scottsdale-az", "population": 258069, "climate": "desert", "season": "Year-round premium appliance demand"},
    {"city": "Tampa", "state": "Florida", "stateAbbr": "FL", "slug": "tampa-fl", "population": 399700, "climate": "subtropical", "season": "Year-round humidity wear and tear"},
    {"city": "Orlando", "state": "Florida", "stateAbbr": "FL", "slug": "orlando-fl", "population": 307573, "climate": "subtropical", "season": "Rental turnover + emergency repairs"},
    {"city": "Miami", "state": "Florida", "stateAbbr": "FL", "slug": "miami-fl", "population": 442241, "climate": "tropical", "season": "High condo and premium appliance demand"},
    {"city": "Atlanta", "state": "Georgia", "stateAbbr": "GA", "slug": "atlanta-ga", "population": 498715, "climate": "humid-subtropical", "season": "Year-round emergency repair demand"},
    {"city": "Charlotte", "state": "North Carolina", "stateAbbr": "NC", "slug": "charlotte-nc", "population": 874579, "climate": "humid-subtropical", "season": "Year-round repair demand"},
    {"city": "Nashville", "state": "Tennessee", "stateAbbr": "TN", "slug": "nashville-tn", "population": 689447, "climate": "humid-subtropical", "season": "STR turnover + emergency repair"},
    {"city": "Las Vegas", "state": "Nevada", "stateAbbr": "NV", "slug": "las-vegas-nv", "population": 641903, "climate": "desert", "season": "Heat-related appliance strain"},
    {"city": "Los Angeles", "state": "California", "stateAbbr": "CA", "slug": "los-angeles-ca", "population": 3898747, "climate": "mediterranean", "season": "Year-round + premium brands"},
    {"city": "San Diego", "state": "California", "stateAbbr": "CA", "slug": "san-diego-ca", "population": 1386932, "climate": "mediterranean", "season": "Year-round + high-end households"},
    {"city": "Denver", "state": "Colorado", "stateAbbr": "CO", "slug": "denver-co", "population": 715522, "climate": "semi-arid", "season": "Winter-related appliance strain"},
    {"city": "Chicago", "state": "Illinois", "stateAbbr": "IL", "slug": "chicago-il", "population": 2696555, "climate": "continental", "season": "Winter urgency + year-round repairs"},
    {"city": "New York", "state": "New York", "stateAbbr": "NY", "slug": "new-york-ny", "population": 8336817, "climate": "humid-continental", "season": "Dense apartment emergency demand"},
    {"city": "Boston", "state": "Massachusetts", "stateAbbr": "MA", "slug": "boston-ma", "population": 675647, "climate": "humid-continental", "season": "Winter wear + premium appliance repair"},
]

REGIONAL_COSTS = {
    "TX": {
        "diagnostic": {"min": 75, "max": 125, "avg": 95},
        "commonRepair": {"min": 140, "max": 320, "avg": 220},
        "emergencyVisit": {"min": 175, "max": 425, "avg": 275},
        "premiumRepair": {"min": 220, "max": 550, "avg": 360},
    },
    "FL": {
        "diagnostic": {"min": 80, "max": 135, "avg": 100},
        "commonRepair": {"min": 150, "max": 340, "avg": 235},
        "emergencyVisit": {"min": 190, "max": 450, "avg": 295},
        "premiumRepair": {"min": 240, "max": 580, "avg": 385},
    },
    "CA": {
        "diagnostic": {"min": 95, "max": 165, "avg": 125},
        "commonRepair": {"min": 180, "max": 420, "avg": 290},
        "emergencyVisit": {"min": 240, "max": 580, "avg": 390},
        "premiumRepair": {"min": 300, "max": 750, "avg": 490},
    },
}

def get_generic_providers(city, state_abbr):
    return [
        {"name": f"{city} Appliance Repair Pros", "rating": 4.9, "reviews": 212, "phone": "(555) 555-2100", "address": f"101 Service Way, {city}, {state_abbr}", "services": ["Refrigerator Repair", "Washer Repair", "Dryer Repair", "Dishwasher Repair"], "yearsInBusiness": 15, "licensed": True, "insured": True},
        {"name": f"Elite Appliance Care {city}", "rating": 4.8, "reviews": 144, "phone": "(555) 555-2200", "address": f"220 Fixit Ave, {city}, {state_abbr}", "services": ["Oven Repair", "Ice Maker Repair", "Garbage Disposal Repair"], "yearsInBusiness": 11, "licensed": True, "insured": True},
        {"name": "Same-Day Home Appliance Co.", "rating": 4.7, "reviews": 119, "phone": "(555) 555-2300", "address": f"78 Repair Rd, {city}, {state_abbr}", "services": ["Same-Day Diagnostics", "Emergency Calls", "Parts Replacement"], "yearsInBusiness": 9, "licensed": True, "insured": True},
        {"name": f"{city} Premium Appliance Techs", "rating": 4.6, "reviews": 76, "phone": "(555) 555-2400", "address": f"415 Restore Blvd, {city}, {state_abbr}", "services": ["Sub-Zero Repair", "Wolf Repair", "High-End Appliance Service"], "yearsInBusiness": 7, "licensed": True, "insured": True},
    ]

def get_faqs(city, state_abbr, costs):
    return [
        {
            "question": f"How much does appliance repair cost in {city}, {state_abbr}?",
            "answer": f"Most appliance repair visits in {city} start with a diagnostic fee of ${costs['diagnostic']['min']}-${costs['diagnostic']['max']}. Common repairs usually land between ${costs['commonRepair']['min']}-${costs['commonRepair']['max']} depending on parts and labor."
        },
        {
            "question": f"Is it worth repairing an appliance in {city}?",
            "answer": f"Usually yes, especially when the repair costs less than 50% of replacement and the unit is still mid-life. In {city}, many refrigerator, washer, dryer, and dishwasher repairs are worth doing if the appliance is otherwise in good shape."
        },
        {
            "question": f"Do appliance repair companies in {city} offer same-day service?",
            "answer": f"Yes. Many appliance repair companies in {city} offer same-day or next-day appointments, especially for refrigerators, washers, and no-heat dryer issues. Emergency visits often start around ${costs['emergencyVisit']['min']}."
        },
    ]

output_dir = Path(__file__).parent.parent / 'data' / 'cities'
output_dir.mkdir(parents=True, exist_ok=True)
all_cities = []
for city_info in CITIES:
    costs = REGIONAL_COSTS.get(city_info['stateAbbr'], REGIONAL_COSTS['TX'])
    data = {
        'slug': city_info['slug'],
        'city': city_info['city'],
        'state': city_info['state'],
        'stateAbbr': city_info['stateAbbr'],
        'population': city_info['population'],
        'applianceRepairSeason': city_info['season'],
        'climateNote': city_info['climate'],
        'costs': costs,
        'providers': get_generic_providers(city_info['city'], city_info['stateAbbr']),
        'faqs': get_faqs(city_info['city'], city_info['stateAbbr'], costs),
        'buyerTips': [
            f"Ask if the diagnostic fee in {city_info['city']} is waived when you approve the repair.",
            'Get the appliance model number ready before calling. It saves time and avoids the usual circus.'
        ],
        'lastUpdated': '2026-04-05'
    }
    with open(output_dir / f"{city_info['slug']}.json", 'w') as f:
        json.dump(data, f, indent=2)
    all_cities.append({'slug': city_info['slug'], 'city': city_info['city'], 'state': city_info['state'], 'stateAbbr': city_info['stateAbbr']})
with open(output_dir / 'cities-index.json', 'w') as f:
    json.dump(all_cities, f, indent=2)
