
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(image):
    response=model.generate_content(image)    
    return response.text
st.set_page_config(page_title="ChitrGPT",page_icon="🤖")
st.header("ChitrGPT")
uploaded_file= st.file_uploader("Choose an image....",type=["jpg","jpeg","png","svg"])
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="uploaded Image",use_column_width=True) 
submit=st.button("Tell me about the Chitr")
if submit:
    response=get_gemini_response(image)
    st.subheader("The response is")
    st.write(response)