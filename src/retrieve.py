from langchain_community.vectorstores import Chroma
from .embed import get_embeddings
from .config import vector_db_dir

def get_retriever():
    embeddings = get_embeddings()

    vectordb = Chroma(
        persist_directory=vector_db_dir, 
        embedding_function=embeddings
    )

    retriever =vectordb.as_retriever(search_kwargs={"k":3}) 
    return retriever 
