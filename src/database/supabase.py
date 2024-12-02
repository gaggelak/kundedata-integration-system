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
        # TODO: Implement conversation saving logic
        # TODO: Generate and store vector embeddings
        result = await supabase.table("chatbot_conversations").insert({
            "conversation_id": conversation_data["conversation_id"],
            "raw_conversation": conversation_data,
            # Add more fields as needed
        }).execute()
        
        return result
    except Exception as e:
        print(f"Error saving conversation: {e}")
        raise e
