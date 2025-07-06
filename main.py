from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from routers import symptoms  # import the router

# Load environment variables from .env file
load_dotenv()

# Example: Access an environment variable
DATABASE_URL = os.getenv("FRONTEND_URL")

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the symptoms router
app.include_router(symptoms.router)
