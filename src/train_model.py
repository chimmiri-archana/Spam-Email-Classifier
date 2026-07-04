import pandas as pd
import joblib
import os
from preprocess import preprocess_text

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("data/SMSSpamCollection", sep="\t", header=None)
data.columns = ["label", "message"]

# Remove duplicates
data = data.drop_duplicates()

# Encode labels
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# Preprocess text
data["message"] = data["message"].apply(preprocess_text)

# Features and target
X = data["message"]
y = data["label"]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


os.makedirs("models", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "models/spam_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")
