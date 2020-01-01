# Import dependecies
import streamlit as st
from transformers import pipeline

# Instantiate pipeline
nlp = pipeline('question-answering')

# User defs
def get_answer(context, question):
    answer = nlp({'question' : question,
            'context' : context
            })['answer']

    return answer

# UI design
st.title("Question Answer System")

# Get context from user
st.header("Context")
context = st.text_area('Put Your Context Here','')

# Get question from user
st.header("Question")
question = st.text_area('Write Your Question Here','')

# Get answer
answer = None
if st.button('Get Answer'):
    answer = get_answer(context, question)

# Display answer in webpage
st.write('Answer:', answer)

