# Chicago VetConnect AI 

An AI powered assistant designed to help military veterans in Chicago find verified local resources such as housing, healthcare, and support services. 

This project uses Retrieval-Augmented Generation (RAG) to ensure answers come directly from trusted documents rather than hallucinated responses. 

# PROBLEM: 
Navigating veteran services can be confusing and time sensitive. Incorrect or outdated information can cause serious harm, especially for individuals experiencing housing instability. 
Chicago VetConnect AI was designed from a user first perspective, priortizing:
- accuracy
- citations
- crisis awareness
- minimal hallucination risk

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

# ARCHITECTURE
User Question 
    |
Crisis Detection Layer
    |
Vector Retrieval (ChromaDB)
    |
Document Context 
    |
LLM Response (Groq/LLama)

# Data Sources 
- Safer Foundation Veteran's Program https://saferfoundation.org
- Chicago Mayor's Office of Veteran Affairs(MOVA) Resource Guide https://www.chicago.gov/city/en/sites/mayors-office-of-veterans-affairs/home.html

# Running Locally (Windows)

### 1. Clone the repo
git clone https://github.com/KayeHowi/Chicago-VetConnect-AI
cd chicago-vetconnect-ai

### 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up your environment variables
Create a `.env` file in the project root and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

### 5. Install and run Ollama (required for embeddings)
Download Ollama from https://ollama.com and then run:
ollama pull nomic-embed-text

### 6. Run the ingestion script (one-time setup)
This populates the vector database with the veteran resource documents.
python ingest.py

### 7. Start the app
uvicorn src.main:app --reload

Once running, open your browser and go to http://127.0.0.1:8000

# Project Goals: 
The goal of this project is to build ethical AI tolls that connect vunerable populations to real services quickly and safely. 

# SAFETY CONSIDERATIONS:
This system minimizes hallucinations risk by:
- Using retrieval augmented generation
- Restricting responses to document context
- Providing citations
- Including crisis detection safeguards 

# What's Next: 
- improve crisis detection without diagnosing the issue.
- improve ranking
- add more documents
- eventually add more states/regions 

# License 
GNU Public License 


