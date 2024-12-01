import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# OpenAI configuration for embeddings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Email configuration
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Database names
TEST_DB = "kundedata_test"
PROD_DB = "kundedata_prod"

# Current environment
IS_DEVELOPMENT = os.getenv("ENVIRONMENT", "development") == "development"