from pypdf import PdfReader
from vector_db.faiss_store import add_documents


def process_pdf(path, user_id):
    reader = PdfReader(path)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    add_documents(user_id, chunks)

    return len(chunks) 





