import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Force load the clean .env file variables
load_dotenv()

app = FastAPI(title="Meridian Agent Portal")

GROQ_KEY = os.getenv("GROQ_API_KEY")

# Check to ensure the key is loaded
if not GROQ_KEY:
    print("⚠️ Critical Warning: Your backend cannot read GROQ_API_KEY from .env!")

client = Groq(api_key=GROQ_KEY)

class TranscriptRequest(BaseModel):
    text: str

@app.post("/generate-quiz")
async def generate_quiz(request: TranscriptRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    prompt = f"Analyze this lecture transcript and create exactly 3 multiple choice questions with answer keys:\n\n{request.text}"
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a professional educational AI assistant for Microsoft Teams."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"quiz": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serves your web interface home screen using a robust absolute path
@app.get("/")
def serve_index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, "static", "index.html")
    
    if not os.path.exists(html_path):
        raise HTTPException(
            status_code=404, 
            detail=f"Frontend file not found! Looked inside: {html_path}"
        )
        
    return FileResponse(html_path)
