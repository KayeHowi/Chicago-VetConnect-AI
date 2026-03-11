# Chicago VetConnect AI 

An AI powered assistant designed to help military veterans in Chicago find verified local resources such as housing, healthcare, and support services. 

This project uses Retrieval-Augmented Generation (RAG) to ensure answers come directly from trusted documents rather than hallucinated responses. 

# Features: 
- Retrieval Augmented Generation
- Crisis detection for urgent situations
- Verified document sources
- Citations included in responses
- FastAPI backend

# Tech Stack: 
- Python
- LangChain
- ChromaDB
- Groq LLM API
- FastAPI
- Vector Embeddings

# Project Structure 

data/raw (contains the documents used)
src/ (contains necessary files)
  - config.py
  - ingest.py
  - embed.py
  - retrieve.py
  - generate.py
  - rag.py
  - main.py
  - init.py

# Data Sources 
- Safer Foundation Veteran's Program https://saferfoundation.org
- Chicago Mayor's Office of Veteran Affairs(MOVA) Resource Guide https://www.chicago.gov/city/en/sites/mayors-office-of-veterans-affairs/home.html

# Running Locally: (Windows)

- git clone https://github.com/KayeHowi/Chicago-VetConnect-AI

- cd chicago-vetconnect-ai

create your venv (very important) and activate it
- python -m venv venv
- venv\Scripts\activate 

- pip install -r requirements.txt 

then run the program (which will build the vector database)
- uvicorn src.main:app --reload 

after application has started, go to 127.0.0.1 and ask the question. 

# Environment Variables (for groq api. get your api key from groq.com)
- create a 'env' file
- add your groq api key in this file.

# Goals: 
The goal of this project is to build ethical AI tolls that connect vunerable populations to real services quickly and safely. 

# What's Next: 
- improve crisis detection without diagnosing the issue.
- improve ranking
- add more documents
- eventually add more states/regions 

# License 
GNU Public License 


