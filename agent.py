# agent.py — Ollama-only version for Nyaya-GPT
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import requests

# 🧩 Helper: Check if Ollama is running
def check_ollama_connection():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.status_code == 200
    except Exception:
        return False

# 🧩 Helper: Get available Ollama models
def get_available_ollama_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            data = response.json()
            return [m["name"] for m in data.get("models", [])]
        return []
    except Exception:
        return []

# ⚖️ Core agent that uses local Ollama models only
def agent(query, use_ollama=True, ollama_model="llama3.1:8b"):
    llm = ChatOllama(model=ollama_model)

    template = """You are Nyaya-GPT, a legal assistant specialized in Indian law.
Answer clearly and accurately using the Bharatiya Nyaya Sanhita (BNS) or the Constitution of India where relevant.

Question: {query}
Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["query"])
    chain = prompt | llm
    response = chain.invoke({"query": query})
    return response.content if hasattr(response, "content") else response
