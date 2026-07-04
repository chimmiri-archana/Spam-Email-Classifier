import joblib
from preprocess import preprocess_text

# Load saved model and vectorizer
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_message(message):
    # Preprocess the input
    message = preprocess_text(message)

    # Convert text to TF-IDF features
    message_vector = vectorizer.transform([message])

    # Predict
    prediction = model.predict(message_vector)[0]

    if prediction == 1:
        return "Spam"
    else:
        return "Ham"


if __name__ == "__main__":
    while True:
        message = input("\nEnter a message: ")

        if message.lower() == "exit":
            print("Goodbye!")
            break

        print("Prediction:", predict_message(message))