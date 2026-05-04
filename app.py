import streamlit as st

st.set_page_config(page_title="AI Agent", page_icon="🧠", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🧠 AI Agent Settings")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.history = []

    st.markdown("---")
    st.write("AI Agent that thinks step-by-step 🚀")

# Title
st.title("🧠 AI Research Agent")

# Memory
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Ask anything...")

# AGENT THINKING (no heavy model)
def agent_think(query):
    steps = f"""
🧠 Step 1: Understanding the question  
➡️ You asked: {query}

🧩 Step 2: Breaking it down  
➡️ This question is about: {query.split()[0] if query else "general topic"}

💡 Step 3: Final Answer  
➡️ Here's a simple explanation:  
{generate_answer(query)}
"""
    return steps

# Simple intelligence
def generate_answer(query):
    query = query.lower()

    if "python" in query:
        return "Python is a powerful programming language used for AI, web, and automation."
    
    elif "ai" in query:
        return "AI stands for Artificial Intelligence, where machines mimic human intelligence."
    
    elif "project" in query:
        return "You can build chatbot, resume parser, or recommendation systems."
    
    elif "data" in query:
        return "Data is information used for analysis and decision-making."
    
    else:
        return "This is a general concept. Try asking about AI, Python, or projects."

# Chat logic
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = agent_think(user_input)

    st.session_state.history.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)