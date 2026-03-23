**🤖 Doc-AI Agent (Agentic RAG System)**
An intelligent Document AI Assistant built using an Agentic RAG (Retrieval-Augmented Generation) architecture, where the system dynamically decides whether to retrieve information from documents or answer directly using an LLM.

**🚀 Overview**
This project implements a smart AI agent capable of:

📄 Understanding and answering questions from uploaded documents (PDFs, files)
🧠 Using LLM reasoning for general queries
⚡ Dynamically deciding between RAG and Direct LLM response
🔍 Providing context-aware and accurate answers
🧠 Architecture (Agentic RAG)

User Query
   ↓
Planner (LLM-based Router)
   ↓
 ┌───────────────┬────────────────┐
 │ Use RAG       │ Direct LLM     │
 │ (Docs needed) │ (General Q)    │
 └───────────────┴────────────────┘
   ↓
Retriever (Vector DB)
   ↓
Context Injection
   ↓
LLM Response

**🔥 Key Features**
✅ Agentic Decision Making (LLM decides RAG vs LLM)
✅ Document Retrieval (RAG) using vector embeddings
✅ Efficient Chunking & Embedding pipeline
✅ Optimized for low-resource systems (8GB RAM)
✅ Hybrid Routing (Rule-based + LLM-based planner)
✅ Fallback mechanisms for stability
✅ Scalable and modular design

⚙️ Tech Stack
🔹 Core AI / ML
Python
LLM (Local / API-based)
Embeddings (Sentence Transformers / MiniLM)
🔹 RAG Pipeline
Vector Database (FAISS / ChromaDB)
Document Loader (PDF/Text)
Text Chunking
🔹 Backend
FastAPI / Flask
🔹 Frontend (Optional)
Streamlit / Custom UI
🧩 How It Works
1. Query Input

User submits a question.

2. Planner (Router)
Decides:
RAG → if document context is needed
LLM → if general knowledge question
3. Retrieval (if RAG)
Relevant chunks fetched from vector DB
4. Context Injection
Retrieved data added to prompt
5. Final Response
LLM generates accurate answer
⚡ Planner Logic (Core Innovation)

The planner uses a hybrid strategy:

🔹 Rule-based filtering (keywords like "document", "PDF")
🔹 LLM-based classification (RAG vs LLM)
🔹 Fallback handling for robustness
📂 Project Structure
doc-ai-agent/
│
├── app.py                # Main application
├── planner.py           # Decision logic (RAG vs LLM)
├── retriever.py         # Vector search logic
├── embeddings.py        # Embedding generation
├── utils/               # Helper functions
├── data/                # Documents
├── vectorstore/         # Stored embeddings
└── README.md
▶️ Setup & Installation
# Clone repo
git clone https://github.com/your-username/doc-ai-agent.git

# Navigate
cd doc-ai-agent

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
⚡ Optimization Techniques
Reduced retrieval (top_k=3)
Lightweight embeddings (MiniLM)
Conditional RAG (avoid unnecessary retrieval)
Streaming responses (optional)
🎯 Use Cases
📄 Document Q&A (PDFs, reports)
🧑‍💼 Business insights from internal docs
📊 Knowledge base assistant
🤖 Personal AI assistant with memory
🧠 Interview Explanation (30 sec)

“I built a Doc-AI agent using an Agentic RAG architecture where an LLM dynamically decides whether to retrieve information from a vector database or answer directly. This improves both accuracy and performance. I implemented document chunking, embeddings, and a hybrid routing planner combining rule-based and LLM-based decision-making.”

🚀 Future Improvements
🔹 Re-ranking for better retrieval
🔹 Memory (chat history)
🔹 Multi-document support
🔹 Source citation in answers
🔹 LangGraph-based agent workflow
📌 Key Learning
Agentic AI design patterns
RAG pipeline optimization
Prompt engineering for decision-making
Trade-offs between latency vs accuracy
