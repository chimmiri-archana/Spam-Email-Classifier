import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("src"))

from predict import predict_message

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Spam Email Classifier")

st.write(
    "Enter an SMS or email message below to check whether it is **Spam** or **Ham**."
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

        prediction = predict_message(message)

        if prediction == "Spam":
            st.error("🚨SPAM MESSAGE")
        else:
            st.success("✅ SAFE")