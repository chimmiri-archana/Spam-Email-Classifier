import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("src"))

from predict import predict_message

st.set_page_config(
    page_title="Spam Message Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Spam Message Classifier")

st.write(
    "Enter an SMS or email message below to check whether it is **Spam** or **Safe**."
)

message = st.text_area(
    "Message",
    height=150,
    placeholder="Type your message here..."
)

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        result = predict_message(message)

        if result == "Spam":
            st.error("🚨 Spam Message.")
            
        else:
            st.success("✅ Safe Message.")