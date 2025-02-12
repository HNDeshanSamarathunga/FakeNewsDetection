import streamlit as st
import joblib

# Load the vectorizer and model
vectorizer = joblib.load("vetorizer.jb")
model = joblib.load("lr_model.jb")

# Set the title of the app
st.title("Fake News Detection")
st.markdown("""
    **Welcome to the Fake News Detection App!**  
    Enter the news article below, and we will help you determine whether it's real or fake.  
    Just type or paste your news article in the text box and click on **"Check News"**.
""")

# Add custom CSS for animated background
st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #ff7a18, #af002d, #320a32);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stTextArea>div>div>textarea {
        background-color: #333333;  
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        width: 100%;
    }

    </style>
""", unsafe_allow_html=True)

# News input area with a more prominent style
news_input = st.text_area("Enter News Article Below:", "", height=200)

# Button to trigger news checking
if st.button("Check News"):
    if news_input.strip():
        # Process the input
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        # Display results with more vibrant feedback
        if prediction[0] == 1:
            st.success("The News is **Real**! 🟢")
        else:
            st.error("The News is **Fake**! 🔴")
    else:
        st.warning("Please enter some text to analyze. 📝")

# Optionally, add a footer with additional information
st.markdown("""
    <footer style="text-align:center;">
        <p>Built with ❤️ using Streamlit and Machine Learning</p>
    </footer>
""", unsafe_allow_html=True)
