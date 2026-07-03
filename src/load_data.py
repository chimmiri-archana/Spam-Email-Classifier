import pandas as pd

# Load dataset
data = pd.read_csv("data/SMSSpamCollection", sep="\t", header=None)

# Rename columns
data.columns = ["label", "message"]

print("Original Shape:", data.shape)

# Remove duplicates
data = data.drop_duplicates()

print("After Removing Duplicates:", data.shape)

# Encode labels
data["label"] = data["label"].map({"ham": 0, "spam": 1})

print("\nFirst 5 Rows:")
print(data.head())