from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Expert Giggle API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "Expert Giggle API is running 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "online"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

@app.post("/activate")
def activate():
    return JSONResponse(
        {
            "success": True,
            "license": "VALID",
            "message": "License Activated"
        }
    )
