import streamlit as st
from langchain_helper import get_eligible_customer_chain, create_vector_db

st.title("Offer eligibility 🌱")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_eligible_customer_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])






