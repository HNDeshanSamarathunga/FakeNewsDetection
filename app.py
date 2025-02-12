import streamlit as st
import joblib

vectorizer = joblib.load("vetorizer.jb")
model = joblib.load("lr_model.jb")

news_input = st.text_area("News Articles:","")

if st.button("Check News"):
    if news_input.strip():
        transform_input = vectorizer.trasform([news_input])
        prediction = model.preict(transform_input)

        if prediction[0]==1:
            st.success("The News is Real !")
        else:
            st.error("The News is Fake !")      
    else:
        st.warning("Please enter some text to analyze")        