from langchain_ollama import OllamaEmbeddings
from .config import embed_model 

def get_embeddings():
    return OllamaEmbeddings (model = embed_model)
