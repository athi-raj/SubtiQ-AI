import pandas as pd

def preprocess(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Convert Yes/No to 1/0
    binary_cols = [
        'THC_Positive_Urine',
        'Cocaine_Positive_Urine',
        'Opioid_Positive_Urine'
    ]

    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    # Encode target
    df['Addiction_Label'] = df['Addiction_Label'].map({
        'Addicted': 1,
        'Not Addicted': 0
    })

    # Drop unnecessary column
    if 'StudentID' in df.columns:
        df = df.drop(columns=['StudentID'])

    return df
