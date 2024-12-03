from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

async def save_conversation(conversation_data: dict):
    try:
        # Validér at vi har et CVR nummer
        cvr = conversation_data.get("customer_info", {}).get("cvr")
        if not cvr:
            raise ValueError("Missing CVR number")
            
        # Gem rå samtale
        result = await supabase.table("chatbot_conversations").insert({
            "cvr": cvr,
            "conversation_id": conversation_data["conversation_id"],
            "raw_conversation": conversation_data,
            "metadata": conversation_data["metadata"]
            # TODO: Tilføj vector embedding senere
        }).execute()
        
        return result
    except Exception as e:
        print(f"Error saving conversation: {e}")
        raise e