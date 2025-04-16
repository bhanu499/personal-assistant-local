
# 💬 Personal Notes Q&A Chatbot (Local or Cloud LLM)

This is a simple yet powerful **personal assistant chatbot** that can answer questions from your own notes using embeddings and any LLM — either cloud-based (OpenAI) or completely local (via [Ollama](https://ollama.com)).

> 🔐 Your data stays private. You own your files and your compute.

---

## 🚀 Features

- 🔍 Ask questions about your own notes
- 📎 Supports `.txt` files (extensible to PDF, CSV, etc.)
- 🤖 Works with OpenAI **or** local models like `deepseek-coder`, `mistral`, etc.
- 💡 Embedding-based semantic search (vector store)
- 🔌 Pluggable LLM backend — add your own easily
- 💻 Runs locally with no internet if using Ollama

---

## 🧱 Project Structure

```
my-chatbot/
├── main.py                     # Main CLI chatbot
├── config.yaml                 # Backend + model config
├── notes/
│   └── my_notes.txt            # Your personal notes (can modify this)
├── llm_backends/
│   ├── __init__.py
│   ├── openai_backend.py       # LLM wrapper for OpenAI
│   └── local_backend.py        # LLM wrapper for Ollama/local model
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. 🔧 Prerequisites

- Python 3.8+
- (Optional) [Ollama](https://ollama.com) for local models like `deepseek-coder`
- Your notes in `notes/my_notes.txt`

---

### 2. 📦 Install Dependencies

```bash
git clone https://github.com/your-username/my-chatbot.git
cd my-chatbot
pip install -r requirements.txt
```

---

### 3. ✍️ Add Your Notes

Replace or edit the contents of `notes/my_notes.txt` with your personal notes or text files you'd like to ask questions about.

---

### 4. ⚙️ Configure the Backend

Edit `config.yaml` to choose your model:

#### 👉 Option 1: Using **OpenAI API**
```yaml
llm_backend: openai
openai_api_key: "sk-..."  # replace with your actual key
```

#### 👉 Option 2: Using **Ollama Local Model**
```yaml
llm_backend: local
local_llm_url: "http://localhost:11434"
local_llm_model: "deepseek-coder:1.5b"  # or "mistral", etc.
```

> Run your model using:
```bash
ollama run deepseek-coder:1.5b
```

---

### 5. 🧠 Run the Chatbot

```bash
python main.py
```

Example:
```
> What is the summary of my project notes?

A: Your project notes discuss the architecture of...
```

Type `exit` to quit.

---

## 🧠 How It Works

1. Splits your notes into chunks
2. Uses **sentence-transformers** to create vector embeddings
3. Stores embeddings in **FAISS** (vector database)
4. When you ask a question:
   - Embeds your query
   - Finds the most relevant chunks
   - Feeds them to the LLM as context to answer

---

## 🛞 Easily Extend or Customize

- ✅ Add support for PDF/Markdown: via `PyMuPDF`, `markdown`, or `pdfplumber`
- ✅ Plug in your own LLM via `llm_backends/`
- ✅ Wrap it in a GUI or convert it into a Chrome extension

---

## 🤖 Example Models to Try with Ollama

```bash
ollama pull deepseek-coder:1.5b
ollama pull mistral
ollama pull llama2
ollama pull phi
```

Then just update `config.yaml` with the name!

---

## 📌 Requirements

```
faiss-cpu
sentence-transformers
openai
requests
pyyaml
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 📄 License

MIT License — free for personal or commercial use.

---

## 🙋 Support & Ideas

Feel free to open issues or pull requests if you want to add:

- Multiple note files
- Browser extension
- GUI frontend
- Whisper integration for voice input

---

> Created with 💡 by [Banu Saladi]
