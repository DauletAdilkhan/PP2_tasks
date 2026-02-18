import json

ferrari = {
    "make": "Ferrari",
    "model": "458 Italia",
    "price": 300000,
    "features": ["V8", "rear-wheel drive", "carbon ceramic brakes"],
    "available": True
}

# writing to a JSON file
with open('ferrari_out.json', 'w') as file:
    json.dump(ferrari, file, indent=4)

print("Saved to ferrari_out.json")

# reading it back to verify
with open('ferrari_out.json', 'r') as file:
    loaded = json.load(file)

print(loaded)
print(loaded["features"])