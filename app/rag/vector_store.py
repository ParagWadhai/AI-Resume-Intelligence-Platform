from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.embeddings import embedding_model


def create_vector_store(text: str, save_path: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = splitter.create_documents([text])

    db = FAISS.from_documents(
        docs,
        embedding_model
    )

    db.save_local(save_path)