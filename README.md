# ⚖️ LexBNS – Bharatiya Nyaya Sanhita Legal Assistant

> 🧠 **An offline, privacy-focused AI assistant** for the *Bharatiya Nyaya Sanhita (BNS), 2023* and the *Constitution of India* — powered entirely by **local Ollama LLMs**.

---

## 📸 Preview

| ⚖️ **LexBNS – Your Local Legal Assistant** |
|:-------------------------------------------:|
| *(Add your screenshot here — e.g., assets/lexbns_ui.png)* |

---

## 🚀 Overview

LexBNS is an **AI-powered legal assistant** that helps users query and interpret India’s **Bharatiya Nyaya Sanhita (BNS), 2023** and the **Constitution of India** — fully **offline**.

It builds upon advanced NLP concepts such as:

- ⚙️ **RAG (Retrieval-Augmented Generation)** – retrieves relevant legal sections  
- 🧩 **ReAct (Reason + Act)** – enables reasoning + contextual retrieval  
- 🔍 **FAISS Vector Database** – for fast semantic search  
- 💻 **Ollama LLMs** – for 100 % local inference (e.g., `llama3.1:8b`)

---

## 🧩 Why LexBNS?

| **Problem** | **LexBNS Solution** |
|:-------------|:--------------------|
| Legal documents are vast and complex | Uses **semantic retrieval** to extract relevant BNS sections |
| Internet-based models risk privacy | Runs **completely offline** via Ollama |
| Chatbots give surface-level replies | Incorporates **ReAct reasoning** for multi-step, contextual answers |
| Difficult to search by section or article | Employs **FAISS embeddings** for legal-term matching |

---

## 🧱 Architecture

```mermaid
graph TD
    A[💬 User Query] --> B[🧠 ReAct Agent]
    B --> C[📘 Retriever (FAISS Vector DB)]
    C --> D[📚 BNS / Constitution PDFs]
    B --> E[🦙 Ollama Model (Llama3.1:8b)]
    E --> F[⚖️ Reasoned Legal Response]
    F --> G[💻 Streamlit UI]
```

---

> The user’s query passes through the **ReAct reasoning loop**,  
> which interacts with a **FAISS-based retriever** and the **local Ollama model**  
> to produce structured, context-aware legal answers.

---

## ⚙️ Setup Guide

> 💡 **LexBNS runs fully offline — no API keys, no internet required.**

---

### ✅ Works On:
- 🪟 **Windows 10 / 11**
- 🐧 **Linux (Ubuntu / Debian)**
- 🍎 **macOS**
- Requires **Python ≥ 3.10**

---

### 🪜 Step 1: Clone the Repository

```bash
git clone https://github.com/GOKULRAM-K/Legal_Bot.git
cd Legal_Bot
```
### ⚙️ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```
### 🦙 Step 3: Install & Start Ollama

Then in terminal
```bash
ollama serve
ollama pull llama3.1:8b
```

> 🟢 Once Ollama is running, your local model (like llama3.1:8b) will be available for LexBNS to process queries.

### 💻 Step 4: Run LexBNS

```bash
streamlit run app.py
```
---

