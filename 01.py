import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")

# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

# https://www.geeksforgeeks.org/with-statement-in-python/

# Example

# class MessageWriter(object):
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def __enter__(self):
#         self.file = open(self.file_name, 'a')
#         print("In MessageWriter __enter__")
#         return self.file
#
#     def __exit__(self, *args):
#         print("In MessageWriter __exit__")
#         self.file.close()
#
# # using with statement with MessageWriter
#
# with MessageWriter('my_file.txt') as xfile:
#     xfile.write('hello world\n')
#
# with MessageWriter('my_file.txt') as xfile:
#     xfile.write('more text\n')
