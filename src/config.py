import os
from dotenv import load_dotenv

load_dotenv()

embed_model = "nomic-embed-text"
llm_model = "llama-3.1-8b-instant"

vector_db_dir = "data/vectordb"

groq_api_key = os.getenv("GROQ_API_KEY") # make sure to get the API key from the Groq account 