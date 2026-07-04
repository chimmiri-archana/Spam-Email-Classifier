# Spam Message Classifier

A Machine Learning project that classifies SMS messages as **Spam** or **Ham** using TF-IDF Vectorization and the Multinomial Naive Bayes algorithm.

## Features

- Spam/Ham message classification
- Text preprocessing using NLTK
- TF-IDF Vectorization
- Multinomial Naive Bayes model
- Streamlit web application

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Git & GitHub

## Project Structure

```
Spam-Message-Classifier/
│
├── app/
├── data/
├── models/
├── src/
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

SMS Spam Collection Dataset

- 5,572 SMS messages
- Labels: Spam / Ham

## Model Performance

**Accuracy:** 96.6%

## Installation

```bash
git clone https://github.com/chimmiri-archana/Spam-Message-Classifier.git
cd Spam-Message-Classifier
pip install -r requirements.txt
streamlit run app/app.py
```

## Sample Prediction

**Input**

```
Congratulations! You have won a FREE iPhone.
```

**Prediction**

```
Spam
```

**Input**

```
Are you coming to college tomorrow?
```

**Prediction**

```
Ham
```

## Future Improvements

- Deploy using Streamlit Cloud
- Improve UI
- Add more machine learning models
- Extend support to spam message detection