from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, Any
import json
from .supabase import save_conversation

app = FastAPI()

class ChatbotWebhook(BaseModel):
    conversation_id: str
    customer_info: Dict[str, Any]
    messages: list[Dict[str, Any]]
    metadata: Dict[str, Any] = {}

@app.post("/webhook/chatbot")
async def receive_chatbot_webhook(webhook_data: ChatbotWebhook):
    try:
        print(f"Received webhook data: {webhook_data}")
        
        # Format data for storage
        conversation_data = {
            "conversation_id": webhook_data.conversation_id,
            "customer_info": webhook_data.customer_info,
            "messages": webhook_data.messages,
            "metadata": webhook_data.metadata
        }
        
        # Save to Supabase
        result = await save_conversation(conversation_data)
        
        return {
            "status": "success", 
            "message": "Webhook data received and saved",
            "id": result.data[0]["id"] if result and result.data else None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/webhook/health")
async def health_check():
    return {"status": "healthy"}