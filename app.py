import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import os
from agent import agent, check_ollama_connection, get_available_ollama_models

# ───────────────────────────────────────────────
# ⚖️ Streamlit Page Configuration (must be first)
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="LexBNS ⚖️",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded",
)

"""
LexBNS – Bharatiya Nyaya Sanhita Legal Assistant
-------------------------------------------------
Local, privacy-focused AI chatbot that helps interpret:
    • Bharatiya Nyaya Sanhita (BNS), 2023
    • The Constitution of India

Powered entirely by local Ollama models – no cloud APIs.
"""

# ───────────────────────────────────────────────
# Streamlit Title
# ───────────────────────────────────────────────
st.title("⚖️ LexBNS – Indian Criminal Law Assistant")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Settings")

    # Check OLLAMA connection
    ollama_available = check_ollama_connection()

    if ollama_available:
        st.success("🟢 Ollama is running locally")
        available_models = get_available_ollama_models()

        if available_models:
            selected_model = st.selectbox(
                "Select Ollama Model:",
                available_models,
                help="Choose from locally installed Ollama models"
            )
        else:
            st.warning(
                "No Ollama models found. "
                "Install one using: `ollama pull llama3.1:8b`"
            )
            selected_model = st.text_input(
                "Enter model name manually:",
                value="llama3.1:8b",
                help="Example: llama3.1:8b, mistral:7b"
            )
    else:
        st.error("🔴 Ollama server not running")
        st.info("Start Ollama by opening a terminal and running:\n\n`ollama serve`")
        selected_model = None

    # Display current configuration
    st.subheader("🧠 Current Configuration")
    if ollama_available:
        st.write(f"**Model:** {selected_model}")
    else:
        st.write("**Model:** None (Ollama not running)")

# Welcome Message
initial_msg = """
### 👩‍⚖️ Welcome to LexBNS
LexBNS is your offline AI assistant for understanding Indian criminal law.

**Available Sources:**
- Bharatiya Nyaya Sanhita (BNS), 2023  
- The Constitution of India

> 💡 *Note:* This chatbot runs entirely on your local machine.
> Please ensure Ollama is running and a model like `llama3.1:8b` is installed.
"""
st.markdown(initial_msg)

# Initialize Conversation Memory
if "store" not in st.session_state:
    st.session_state.store = []

store = st.session_state.store

# Display existing chat history
for message in store:
    avatar = "👩‍⚖️" if message.type == "ai" else "🗨️"
    with st.chat_message(message.type, avatar=avatar):
        st.markdown(message.content)

# Chat Input Section
if prompt := st.chat_input("Ask your question about BNS or the Constitution..."):
    # Display user message
    st.chat_message("user", avatar="🗨️").markdown(prompt)

    # Show “thinking” message
    thinking_placeholder = st.chat_message("assistant", avatar="⚖️")
    thinking_placeholder.markdown("🤔 Thinking...")

    # Store user message
    store.append(HumanMessage(content=prompt))

    try:
        if not ollama_available:
            response_text = "⚠️ Ollama is not running. Start it using `ollama serve`."
        elif not selected_model:
            response_text = "⚠️ No model selected. Please select or install an Ollama model."
        else:
            response_text = agent(prompt, use_ollama=True, ollama_model=selected_model)

        response = AIMessage(content=response_text)

    except Exception as e:
        response = AIMessage(content=f"❌ Error: {str(e)}")

    # Save and display AI response
    store.append(response)
    thinking_placeholder.markdown(response.content)

# ───────────────────────────────────────────────
# Footer (Credits)
# ───────────────────────────────────────────────
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center;color:gray;font-size:12px;margin-top:20px;'>
        ⚖️ <b>LexBNS</b> | Local AI Assistant for Indian Criminal Law<br>
        💡 Powered by <b>Ollama</b> | Works 100% Offline
    </div>
    """,
    unsafe_allow_html=True,
)

# ───────────────────────────────────────────────
# Bottom-left Team Credits
# ───────────────────────────────────────────────
st.markdown(
    """
    <style>
        .team-box {
            position: fixed;
            bottom: 10px;
            left: 15px;
            background-color: rgba(240,240,240,0.9);
            padding: 8px 14px;
            border-radius: 10px;
            box-shadow: 0 0 6px rgba(0,0,0,0.1);
            font-size: 12px;
            color: #333;
        }
        .team-box b {
            color: #000;
        }
    </style>
    <div class='team-box'>
        <b>Team LexBNS:</b><br>
        Gokul Ram K<br>
        Aishwarya Sreenivasan<br>
        Shyam Karthinathan<br>
        <b>Guide:</b> Dr. Sajidha A
    </div>
    """,
    unsafe_allow_html=True
)
