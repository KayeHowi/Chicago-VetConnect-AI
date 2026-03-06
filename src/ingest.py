from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma 
from src.embed import get_embeddings
from src.config import vector_db_dir

def ingest_docs():
    
    loader = DirectoryLoader("data", glob=".pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    chunks = splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documenets=chunks,
        embeddings=get_embeddings(), 
        persist_directory=vector_db_dir
    
    )
    vectordb.peresist()
