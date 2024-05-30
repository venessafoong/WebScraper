from fastapi import FastAPI
from models import Property
import json
import uvicorn

app = FastAPI()

with open('./API/property.json', 'r') as f:
    data = json.load(f)
    properties = data['property']

# Get all addresses
@app.get('/property')
async def get_addresses():
    return data

# Add a property
@app.post('/property/add')
async def addProperty(property: Property):
    if [p['id'] for p in properties]:
        last_id = max([p['id'] for p in properties])
    else:
        last_id = 0
        
    new_property = {
        "id": last_id + 1,
        "address": property.address,
        "price": property.price
    }
    properties.append(new_property)

    with open('property.json','r+') as f:
        json.dump(data, f, indent = 4)

    return new_property

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')