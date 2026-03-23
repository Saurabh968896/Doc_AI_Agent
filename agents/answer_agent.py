import ollama
from agents.retrieval_agent import retrieve_documents
from cache.redis_cache import get_cache, set_cache


def generate_answer(user_id, question, model="phi3"):
    """
    Answer agent with caching
    """

    cache_key = f"{user_id}:{model}:{question}"

    # -----------------------------
    # Step 1: Check cache
    # -----------------------------
    cached_answer = get_cache(cache_key)

    if cached_answer:
        return cached_answer

    # -----------------------------
    # Step 2: Generate answer (fallback)
    # -----------------------------
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": question}]
    )

    answer = response["message"]["content"]

    # -----------------------------
    # Step 3: Store in cache
    # -----------------------------
    set_cache(cache_key, answer)

    return answer