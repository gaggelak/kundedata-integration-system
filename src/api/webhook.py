from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, Any
import json

app = FastAPI()

class ChatbotWebhook(BaseModel):
    conversation_id: str
    customer_info: Dict[str, Any]
    messages: list[Dict[str, Any]]
    metadata: Dict[str, Any] = {}

@app.post("/webhook/chatbot")
async def receive_chatbot_webhook(webhook_data: ChatbotWebhook):
    try:
        # Log raw data for debugging
        print(f"Received webhook data: {webhook_data}")
        
        # TODO: Validate CVR/company_id
        # TODO: Generate vector embeddings
        # TODO: Save to Supabase
        
        return {"status": "success", "message": "Webhook data received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/webhook/health")
async def health_check():
    return {"status": "healthy"}
