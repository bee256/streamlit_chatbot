import streamlit as st
import ollama


# Generator for Streaming Tokens
def response_generator():
    ollama_response = ollama.chat(model=st.session_state.sel_mod['model'], stream=True, messages=st.session_state.messages)
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

    # Get the list of ollama modes installed on machine
    models = ollama.list()['models']
    # Create a dict with the name of the mode as key
    models_dict = {item['name']: item for item in models}

    sel_mod_name = st.selectbox("Choose LLM:", models_dict.keys(), on_change=clear_messages)
    sel_mod = models_dict[sel_mod_name]
    st.session_state.sel_mod = sel_mod

    st.write(models_dict)


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

