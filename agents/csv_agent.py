import pandas as pd
from embeddings.embedding_model import create_embedding
from vector_db.faiss_store import add_vector


def process_csv(user_id, file_path):
    """
    Process CSV file:
    Convert each row into text and store embeddings
    """

    df = pd.read_csv(file_path)

    chunks = []

    # Convert each row into sentence
    for _, row in df.iterrows():
        row_text = " ".join([str(value) for value in row.values])
        chunks.append(row_text)

    # Store vectors
    for chunk in chunks:
        vector = create_embedding(chunk)
        add_vector(user_id, vector, chunk)

    return len(chunks)