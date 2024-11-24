import streamlit as st
import numpy as np

with st.chat_message("user", avatar="💖"):
    st.write("Hello 👋")

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))

# With statement is same as writing
# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))
