# fastapi_neon/main.py

from fastapi import FastAPI

app = FastAPI(title="Fastapi-PIAIC-Helloworld", 
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])


@app.get("/")
def read_root():
    return {"PIAIC": "HELLO WORLD WITH PIAIC"}
@app.get("/piaic")
def read_root():
    return {"Welcome": "In PIAIC"}