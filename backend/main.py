from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

# Import routers - make sure these are correct
from routers import auth, tenders, ai

load_dotenv()

app = FastAPI(title="Pomen API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers - ADD THESE LINES
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(tenders.router, prefix="/api/tenders", tags=["tenders"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Pomen API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)