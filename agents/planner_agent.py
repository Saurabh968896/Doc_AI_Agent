import requests
from agents.retrieval_agent import retrieve_documents
from vector_db.faiss_store import user_docs

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


# ✅ CLEAN TEXT (fix UI spacing issue)
def clean_text(text):
    text = text.replace("\n", " ")
    return " ".join(text.split())


# ✅ LLM CALL (FIX TIMEOUT + STABILITY)
def call_llm(prompt, model="phi3"):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60   # 🔥 increased timeout
        )

        return response.json().get("response", "")

    except Exception as e:
        print("LLM ERROR:", e)
        return "LLM not available"


# ✅ MAIN PLANNER (STRICT CONTROL)
def plan_and_execute(user_id, question, model):

    # 🔹 If no document → LLM
    if user_id not in user_docs:
        return call_llm(question, model)

    docs, scores = retrieve_documents(user_id, question)

    if not docs:
        return call_llm(question, model)

    best_score = scores[0]

    print("DEBUG SCORE:", best_score)   # 🔥 debug

    # =========================
    # 🎯 STRICT RAG (NO LLM)
    # =========================
    if best_score < 1.2:
        return clean_text(docs[0])

    # =========================
    # ⚖️ SOFT RAG (LLM + CONTEXT)
    # =========================
    elif best_score < 1.8:
        context = clean_text(" ".join(docs[:2]))

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Give a clear and concise answer.
"""
        return call_llm(prompt, model)

    # =========================
    # 🤖 PURE LLM
    # =========================
    else:
        return call_llm(question, model)