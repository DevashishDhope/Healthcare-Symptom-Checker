from dotenv import load_dotenv

# Load environment variables immediately
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import symptom_routes

app = FastAPI(
    title="Healthcare Symptom Checker",
    description="AI-powered symptom checker for educational purposes.",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity in this demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(symptom_routes.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Healthcare Symptom Checker API is running."}
