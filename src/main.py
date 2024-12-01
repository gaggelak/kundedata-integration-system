from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Kundedata Integration System")

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

@app.get("/")
async def root():
    return {"message": "Kundedata Integration System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)