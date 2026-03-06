# Chicago VetConnect AI (Version 1)
AI powered resource assistant helping Chicago military veterans quickly find housing, healthcare, and support services within Chicago and the Greater Chicago area. 

This project uses Retrieval Augmented Generation (RAG) to provide grounded answers based on verified documents from local and federal veteran support organizations. 

Crisis awareness and minimized hallucination risk are the key safety consideratons of this project. 

PROBLEM: 
Navigating veteran services can be confusing and time sensitive. Incorrect or outdated information can cause serious harm, especially for individuals experiencing housing instability. 
Chicago VetConnect AI was designed from a user first perspective, priortizing:
- accuracy
- citations
- crisis awareness
- minimal hallucination risk

FEATURES: 
- Retrieval Augmented Generation (RAG)
- Vector searh with ChromaDB
- local embeddings 
- Crisis phrase detection and emergency guidance
- Source citations 
- FastAPI backend
- Groq powered LLM responses

Stack:
- Python
- FastAPI
- Langchain
- ChromaDB
- Groq LLM API
- Ollama (local models)

ARCHITECTURE
User Question 
    |
Crisis Detection Layer
    |
Vector Retrieval (ChromaDB)
    |
Document Context 
    |
LLM Response (Groq/LLama)

SETUP:
Clone the repo: 
git clone https://github.com/KayeHowi/Chicago-VetConnect-AI
cd chicago_vetconnect_ai

Create environment:
python -m venv venv 
venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Create the .env file (you will need your own Groq API key. Get it from Groq.com)
groq_api_key=your_api_key_here

Ingest documents:
python src/ingest.py

Run server:
uvicorn src.main.app --reload

Open: 
http://127.0.0.1:8000

Then ask your question and get a response. 

SAFETY CONSIDERATIONS:
This system minimizes hallucinations risk by:
- Using retrieval augmented generation
- Restricting responses to document context
- Providing citations
- Including crisis detection safeguards 

Upcoming Updates (version 2):
- Add additional Chicago area veteran resource documents
- Improve retrieval ranking
- Add conversation memory
- Deploy production demo
- Improve crisis detection and response 

Goal: 
The goal of this project is to build ethical AI tools that connect vunerable populations to real services quickly and safely. 

Data Sources: 
A Safer Haven Veteran Resources Guide
Chicago Mayor's Office of Veteran Affairs Resource Guide 

License
This project is licensed under the GNU General Public License. 