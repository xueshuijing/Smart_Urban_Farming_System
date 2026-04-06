from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Urban Farming API is running"}

@app.get("/plants")
def get_plants():
    return [
        {
            "id": 1,
            "name": "Tomato",
            "water": "Medium",
            "sunlight": "Full Sun"
        }
    ]

