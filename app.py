
import streamlit as st
import pickle
import re
import string

# Text preprocessing function
def wordopt(text):
    # Convert to lowercase
    if isinstance(text, list):
        text = ' '.join(text)
    text = text.lower()
    # Remove content within square brackets
    text = re.sub(r'\[.*?\]', '', text)
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove punctuation
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    # Remove words with numbers
    text = re.sub(r'\w*\d\w*', '', text)
    # Remove non-word characters and extra whitespace
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Streamlit app title
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stTextInput textarea {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
            width: 100%;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            font-size: 36px;
        }
        .stTextInput label {
            font-size: 16px;
            color: #333;
        }
        .stWrite {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.title('Fake News Detection')

# Input text box for the user to enter news text
user_input = st.text_area("Enter the news text", height=200)

# Preprocess the input text
input_text = wordopt(user_input)

# Load the pre-trained TfidfVectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Transform the input text using the pre-trained vectorizer
input_vector = vectorizer.transform([input_text])

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Predict the input text's class (fake or real)
prediction = model.predict(input_vector)

# Button to trigger prediction
if st.button('Predict'):
    if prediction == 0:
        st.write('<p class="stWrite">The news is Real</p>', unsafe_allow_html=True)
    else:
        st.write('<p class="stWrite">The news is Fake</p>', unsafe_allow_html=True)
