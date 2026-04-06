import json
import os

cities = [
    {"city": "New York", "state": "NY", "pop": "8.8M"},
    {"city": "Los Angeles", "state": "CA", "pop": "3.8M"},
    {"city": "Chicago", "state": "IL", "pop": "2.7M"},
    {"city": "Houston", "state": "TX", "pop": "2.3M"},
    {"city": "Phoenix", "state": "AZ", "pop": "1.6M"},
    {"city": "Philadelphia", "state": "PA", "pop": "1.6M"},
    {"city": "San Antonio", "state": "TX", "pop": "1.4M"},
    {"city": "San Diego", "state": "CA", "pop": "1.3M"},
    {"city": "Dallas", "state": "TX", "pop": "1.3M"},
    {"city": "San Jose", "state": "CA", "pop": "1.0M"},
    {"city": "Austin", "state": "TX", "pop": "961K"},
    {"city": "Jacksonville", "state": "FL", "pop": "949K"},
    {"city": "Fort Worth", "state": "TX", "pop": "918K"},
    {"city": "Columbus", "state": "OH", "pop": "905K"},
    {"city": "Indianapolis", "state": "IN", "pop": "887K"},
    {"city": "Charlotte", "state": "NC", "pop": "874K"},
    {"city": "San Francisco", "state": "CA", "pop": "815K"},
    {"city": "Seattle", "state": "WA", "pop": "737K"},
    {"city": "Denver", "state": "CO", "pop": "715K"},
    {"city": "Washington", "state": "DC", "pop": "689K"}
]

services = [
    "Full Interior Detail",
    "Exterior Hand Wash & Wax",
    "Paint Correction & Ceramic Coating",
    "Engine Bay Cleaning",
    "Headlight Restoration",
    "Odor Removal & Sanitization",
    "Leather Conditioning",
    "Pet Hair Removal Specialist",
    "Clay Bar Treatment",
    "Wheels & Tires Deep Clean"
]

data_dir = "data/cities"
os.makedirs(data_dir, exist_ok=True)

for city_info in cities:
    city_slug = city_info["city"].lower().replace(" ", "-")
    city_data = {
        "city": city_info["city"],
        "state": city_info["state"],
        "slug": city_slug,
        "title": f"Mobile Detailing in {city_info['city']}, {city_info['state']} | Professional Car Care at Your Door",
        "description": f"Top-rated mobile detailing services in {city_info['city']}. We come to you! Interior detailing, paint correction, ceramic coating, and more. Serving {city_info['city']} and surrounding areas.",
        "services": services,
        "price_estimate": "$150 - $450",
        "turnaround_time": "2-4 hours",
        "why_us": [
            "We Come to You: At home, work, or the gym.",
            "Professional Equipment: Industrial steam cleaners, high-end vacuums, and eco-friendly soaps.",
            "Certified Detailers: Experienced professionals who treat your car like their own.",
            "Hassle-Free Booking: Fast, easy, and transparent pricing."
        ],
        "faqs": [
            {
                "question": f"How long does a full detail take in {city_info['city']}?",
                "answer": "A standard full interior and exterior detail usually takes between 3 to 5 hours, depending on the size and condition of the vehicle."
            },
            {
                "question": "Do you need access to water or electricity?",
                "answer": "Most of our mobile units are fully self-contained with their own water tanks and generators, but we'll confirm this when you book!"
            },
            {
                "question": "Do you offer ceramic coating?",
                "answer": f"Yes, we provide professional ceramic coating services in {city_info['city']} to protect your car's paint for years to come."
            }
        ]
    }
    
    with open(f"{data_dir}/{city_slug}.json", "w") as f:
        json.dump(city_data, f, indent=2)

print(f"Generated {len(cities)} city pages in {data_dir}")
