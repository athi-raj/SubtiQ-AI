import pandas as pd
from preprocess import preprocess
from train_model import train_model
from predict import predict

# Load sample dataset (use small CSV, not full data)
df = pd.read_csv("../dataset_sample.csv")

# Preprocess
df = preprocess(df)

# Train model
model = train_model(df)

# Example prediction (sample input)
sample_input = df.drop('Addiction_Label', axis=1).iloc[0].values
result = predict(model, sample_input)

print("Sample Prediction:", result)
