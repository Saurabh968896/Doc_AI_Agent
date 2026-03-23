from vector_db.faiss_store import search_documents


def retrieve_documents(user_id, query):
    return search_documents(user_id, query)