import uuid

companies = [
    {
        "id": str(uuid.uuid4()),
        "name": "Acme Real Estate",
        "type": "Real Estate",
        "email": "contact@acmereal.com"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Sunrise Builders",
        "type": "Construction",
        "email": "info@sunrisebuild.com"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Blue Horizon Brokers",
        "type": "Broker",
        "email": "support@bluehorizon.co"
    }
]

properties = [
    # Acme Real Estate
    {
        "id": str(uuid.uuid4()),
        "name": "Ocean View Apartment",
        "address": "123 Beach Ave",
        "price": 250000,
        "size": "120 sqm",
        "company": "Acme Real Estate"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Downtown Loft",
        "address": "456 City Center",
        "price": 320000,
        "size": "95 sqm",
        "company": "Acme Real Estate"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Suburban House",
        "address": "789 Maple Drive",
        "price": 290000,
        "size": "150 sqm",
        "company": "Acme Real Estate"
    },

    # Sunrise Builders
    {
        "id": str(uuid.uuid4()),
        "name": "Mountain Cabin",
        "address": "111 Pine Hill",
        "price": 180000,
        "size": "80 sqm",
        "company": "Sunrise Builders"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Lakeside Villa",
        "address": "222 Lake Road",
        "price": 450000,
        "size": "200 sqm",
        "company": "Sunrise Builders"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Modern Duplex",
        "address": "333 Oak Lane",
        "price": 370000,
        "size": "140 sqm",
        "company": "Sunrise Builders"
    },

    # Blue Horizon Brokers
    {
        "id": str(uuid.uuid4()),
        "name": "Urban Condo",
        "address": "1000 Skyline Blvd",
        "price": 310000,
        "size": "85 sqm",
        "company": "Blue Horizon Brokers"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Studio Flat",
        "address": "1010 Downtown Street",
        "price": 210000,
        "size": "60 sqm",
        "company": "Blue Horizon Brokers"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Penthouse Suite",
        "address": "1020 Luxury Towers",
        "price": 650000,
        "size": "220 sqm",
        "company": "Blue Horizon Brokers"
    }
]

def add_company(company_data):
    company_data["id"] = str(uuid.uuid4())
    companies.append(company_data)

def get_companies():
    return companies

def add_property(property_data):
    property_data["id"] = str(uuid.uuid4())
    properties.append(property_data)

def get_properties():
    return properties
