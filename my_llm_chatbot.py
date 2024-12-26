import streamlit as st
from langchain_groq import ChatGroq

# Set up the Streamlit page title
st.title("LLM ChatBot")

# Access the Groq API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize the Groq model
llm = ChatGroq(
    model_name="llama-3.1-70b-versatile",
    temperature=0.7,  # Adjust the creativity of responses
    groq_api_key=GROQ_API_KEY,
)

# Initialize session state for model and messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history
# Display existing chat history with properly styled labels
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Response:** {message['content']}")

# Input box for user prompt
if user_prompt := st.chat_input("What do you want to ask?"):
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.markdown(f"**You:** {user_prompt}")

    # Get assistant's response
    response = llm.invoke(
        [  # Pass the entire conversation history
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
    )
    st.markdown(f"**Response:** {response.content}")

    # Add assistant response to the session state
    st.session_state.messages.append({"role": "assistant", "content": response.content})
