
from transformers import pipeline

cy_en_model = "Helsinki-NLP/opus-mt-cy-en"
en_cy_model = "fine-tuned-opus-mt-en-cy-7"

zh_en_pipe = pipeline("translation",model = cy_en_model)
en_zh_pipe = pipeline("translation", model = en_cy_model)

import streamlit as st

st.title("Translation Application")

# Select language pairs 
language_pair = st.selectbox(
    "Choose language pair:",
    ["English to Welsh","Welsh to English"],
    placeholder="Select an option"
    )

translation = None 

# Input Text 
input_text = st.text_area("Enter the text to translate : ")

if st.button("Translate"):
    if input_text:  
        if language_pair == "English to Welsh":
            translation = en_zh_pipe(input_text)[0]['translation_text']
        elif language_pair == "Welsh to English":
            translation = zh_en_pipe(input_text)[0]['translation_text']
    else:
        st.warning("Please enter text to translate.")

st.write("Translation : ",translation)

