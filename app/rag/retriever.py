from langchain_community.vectorstores import FAISS
from app.rag.embeddings import embedding_model


def retrieve(query, db_path):

    db = FAISS.load_local(
        db_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    return docs