from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI(title="Pokedex API")

# Load the Pokedex data
DATA_FILE = "pokedex.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

pokedex_data = load_data()

@app.get("/")
def home():
    return {"message": "Welcome to the Pokedex API! Access /pokemon to see all entries."}

@app.get("/pokemon")
def get_all_pokemon():
    """Returns a list of all available Pokemon names."""
    return list(pokedex_data.keys())

@app.get("/pokemon/{name}")
def get_pokemon_by_name(name: str):
    """Returns full details for a specific Pokemon."""
    # Convert input to lowercase to match JSON keys
    name_lower = name.lower()
    
    if name_lower not in pokedex_data:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    return pokedex_data[name_lower]

if __name__ == "__main__":
    import uvicorn
    # Start the server on localhost:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
