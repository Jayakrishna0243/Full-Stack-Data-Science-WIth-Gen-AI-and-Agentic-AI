import streamlit as st
from ollama import Client
client=(host="http://localhost:11434")
st.set_page_config(
    page_title="custom MR JAI-ollama",
    layout="centered"
)
st.title("MR JAI -ollama app")
prompt=st.text_area("Enter your prompt:",height=300)
if st.button("Generate Response"):
   if prompt.strip()=="deepseek-r1:1.5b":
    st.warning("Please enter a prompt.")
   else:
     with st.spinner("Thinking...."):
        response=client.chat(
          model="deepseek-r1:1.5b",
          messages=[
            {"role":"user","content":prompt}
        ]
    )
     st.success("response generated!")
     st.write(response["message"]["content"])
    
