from fastapi import FastAPI
from models import Property
import json

app = FastAPI()

with open('property.json', 'r') as f:
    properties = json.load(f)

# Get all addresses
@app.get('/property')
async def get_addresses():
    return properties

# Add a property
@app.post('/property/add')
async def addProperty(property: Property):
    new_property = {
        "id": max([p['id'] for p in properties['property']]) + 1,
        "address": property.address,
        "price": property.price
    }
    
    properties['property'].append(new_property)

    with open('property.json','r+') as f:
        json.dump(properties, f, indent = 4)

    return new_property