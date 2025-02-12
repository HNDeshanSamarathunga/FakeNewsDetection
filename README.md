
# Fake News Detection Using Machine Learning

## 🚀 Project Overview
This project demonstrates the creation of a **Machine Learning-based Fake News Detection** system using **Natural Language Processing (NLP)** and **Logistic Regression**. The application is built using **Streamlit** for an interactive, real-time user interface that allows users to classify news articles as **real** or **fake**.

With the rise of misinformation, this system aims to provide a simple, accessible tool for users to verify the authenticity of news articles.

## ✨ Key Features:
- **Interactive UI**: Built with **Streamlit** for seamless user interaction.
- **Lightweight**: Easy to deploy and use.

## 🔧 Technologies Used:
- **Machine Learning**: Logistic Regression for binary classification of real vs fake news.
- **Natural Language Processing**: TF-IDF vectorizer to transform news text into numerical features.
- **Web Application**: **Streamlit** to build the interactive frontend.
- **Model Management**: **Joblib** for saving and loading the model and vectorizer.

## 🛠️ Installation Guide

### Prerequisites:
- Python 3.x
- Virtual environment (recommended for isolated dependencies)

### Steps to Set Up:
1. Clone this repository:
   ```bash
   git clone https://github.com/HNDeshanSamarathunga/fake-news-detection.git
   ```
2. Navigate to the project folder:
   ```bash
   cd fake-news-detection
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```
5. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage Instructions:
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. **Enter a news article** in the input field and press **"Check News"**.
3. **Get real-time feedback** with a visual representation of whether the news is **real** or **fake**.

## 💡 Contributing
Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to **fork the repository** and submit a **pull request**.

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🔗 Link to Demo
- [Link to Project Demo](#)  *(Optional)*
