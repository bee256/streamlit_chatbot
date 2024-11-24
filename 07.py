import streamlit as st
import ollama


# Generator for Streaming Tokens
def response_generator():
    ollama_response = ollama.chat(model='mistral-nemo', stream=True, messages=st.session_state.messages)
    for partial_resp in ollama_response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token


def clear_messages():
    st.session_state.messages = []


with st.sidebar:
    st.title("💬 FG Chatbot")
    if st.button("New chat"):
        clear_messages()

# Initialize chat history
if "messages" not in st.session_state:
    clear_messages()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    if prompt.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.session_state["full_message"] = ""
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})

