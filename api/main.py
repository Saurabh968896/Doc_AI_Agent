from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from agents.document_agent import process_pdf
from agents.planner_agent import plan_and_execute

app = FastAPI()


# ---------------- UI ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>AI Document Assistant</title>
        <style>
            body {
                font-family: Arial;
                margin: 40px;
                background: #f5f5f5;
            }

            .container {
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            h1 {
                text-align: center;
            }

            input, textarea, select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                border: 1px solid #ccc;
            }

            button {
                padding: 10px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background: #0056b3;
            }

            #answer {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                margin-top: 10px;
                line-height: 1.6;
                white-space: normal;
                word-wrap: break-word;
            }

            #upload_status {
                color: green;
                margin-top: 5px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>AI Document Assistant</h1>

            <h2>Upload Document</h2>
            <input id="user_id_upload" placeholder="User ID"/>
            <input type="file" id="file"/>
            <button onclick="upload()">Upload</button>
            <p id="upload_status"></p>

            <h2>Ask Question</h2>
            <input id="user_id_query" placeholder="User ID"/>

            <select id="model">
                <option value="phi3">phi3</option>
                <option value="llama3">llama3</option>
            </select>

            <textarea id="question" placeholder="Enter your question"></textarea>

            <button onclick="ask()">Ask</button>

            <div id="answer">Your answer will appear here...</div>
        </div>

        <script>
            async function upload() {
                const user_id = document.getElementById("user_id_upload").value;
                const file = document.getElementById("file").files[0];

                if (!user_id || !file) {
                    alert("Please provide user_id and file");
                    return;
                }

                const formData = new FormData();
                formData.append("file", file);
                formData.append("user_id", user_id);

                const res = await fetch("/upload", {
                    method: "POST",
                    body: formData
                });

                const data = await res.json();

                document.getElementById("upload_status").innerText =
                    "Uploaded successfully. Chunks: " + data.chunks;
            }

            async function ask() {
                const user_id = document.getElementById("user_id_query").value;
                const question = document.getElementById("question").value;
                const model = document.getElementById("model").value;

                if (!user_id || !question) {
                    alert("Please provide user_id and question");
                    return;
                }

                document.getElementById("answer").innerText = "Thinking...";

                const res = await fetch("/query", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        user_id,
                        question,
                        model
                    })
                });

                const data = await res.json();

                // ✅ FIX FORMATTING ISSUE HERE
                const cleanAnswer = data.answer
                    ? data.answer.replace(/\\n+/g, " ")
                    : "No answer found";

                document.getElementById("answer").innerText = cleanAnswer;
            }
        </script>
    </body>
    </html>
    """


# ---------------- UPLOAD ----------------
@app.post("/upload")
async def upload(file: UploadFile = File(...), user_id: str = Form(...)):
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    chunks = process_pdf(path, user_id)

    return {"message": "Uploaded", "chunks": chunks}


# ---------------- QUERY ----------------
class Query(BaseModel):
    user_id: str
    question: str
    model: str


@app.post("/query")
def query(q: Query):
    answer = plan_and_execute(q.user_id, q.question, q.model)
    return {"answer": answer}