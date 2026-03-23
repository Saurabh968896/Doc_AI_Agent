from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

user_docs = {}
user_index = {}


def add_documents(user_id, texts):
    embeddings = model.encode(texts)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    user_docs[user_id] = texts
    user_index[user_id] = index


def search_documents(user_id, query):
    if user_id not in user_index:
        return [], []

    q_emb = model.encode([query])
    D, I = user_index[user_id].search(np.array(q_emb), k=2)

    docs = [user_docs[user_id][i] for i in I[0]]
    scores = D[0]

    return docs, scores