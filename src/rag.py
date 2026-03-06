from asyncio.log import logger
from langchain_classic.chains import RetrievalQA
from .retrieve import get_retriever
from .generate import build_prompt, get_llm 

crisis_phrases = [
    "I want to kill myself", 
    "I want to die", 
    "I am going to kill myself",
    "I plan to hurt myself", 
    "I don't want to live anymore", 
    "It would be better if I were dead",
    "Life isn't worth living anymore",
    "I am in so much pain I want to die",
    "I can't go on living anymore",
    "i'm in immediate danger"
]
def is_explicit_crisis(question: str) -> bool:
    question_lower = question.lower()
    for phrase in crisis_phrases:
        if phrase in question_lower:
            return True
    return False

def ask_question(question:str):
    #explicit crisis detection
    if is_explicit_crisis(question):
        return """
It sounds like you may be in crisis. If you're in immediate danger, please call 911. 
If you're in need of mental health support, you can call the Veteran's Crisis line at 988 and press 1
or text 838255. You can also call 311 for non-emergency assistance in Chicago."""
    retriever = get_retriever()
    llm = get_llm()
    docs = retriever.get_relevant_documents(question)
    if len(docs) == 0:
        return """I'm sorry, I couldn't find any information related to your question. Please try another question."""
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type_kwargs={"prompt": build_prompt()}, return_source_documents=True)
    answer = qa_chain.run(question)

    sources =set()
    for doc in docs:
        source = doc.metadata.get("source", "Resource document")
        sources.add(source)

    citation_text = "\n\nSources:\n"
    for s in sources:
        citation_text += f" - {s}\n"

    footer =  """
    "\n\nIf this is an emergency:
    Please call 911 immediately. 
    You can also call the Veteran's Crisis line at 988 (Press 1)
    If in Chicago, call city services at 311 for emergency shelter assistance and other non ememrgency resources.
    """
    logger.info("ask_question() triggered")
    return answer + citation_text + footer 


