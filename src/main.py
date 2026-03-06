from fastapi import FastAPI
from .rag import ask_question 

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to the Chicago Veteran's Resource Assistant API. Please use the /ask endpoint to ask a question about veteran's resources in Chicago."}

@app.get("/ask")
def ask(question: str):
    answer = ask_question(question)
    return {"response": answer}
