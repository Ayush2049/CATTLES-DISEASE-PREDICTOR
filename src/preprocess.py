import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    """Preprocess the data and return processed df, encoders, and feature columns"""
    
    # Make a copy to avoid modifying original
    df = df.copy()
    
    # Encode target
    le = LabelEncoder()
    df['Disease'] = le.fit_transform(df['Disease'])

    # Get all unique symptoms
    unique_symptoms = set(df['Symptom 1']).union(df['Symptom 2']).union(df['Symptom 3'])
    unique_symptoms = sorted(list(unique_symptoms))  # Sort for consistency
    
    # One-hot encode symptoms
    for symptom in unique_symptoms:
        df[symptom] = 0

    for i, row in df.iterrows():
        for col in ['Symptom 1', 'Symptom 2', 'Symptom 3']:
            if row[col] in unique_symptoms:
                df.loc[i, row[col]] = 1

    df.drop(['Symptom 1', 'Symptom 2', 'Symptom 3'], axis=1, inplace=True)

    # One-hot encode Animal type
    df = pd.get_dummies(df, columns=['Animal'])

    # Scale numerical values
    scaler = StandardScaler()
    df[['Age', 'Temperature']] = scaler.fit_transform(df[['Age', 'Temperature']])

    # Get feature columns (everything except Disease)
    feature_columns = [col for col in df.columns if col != 'Disease']
    
    return df, le, scaler, unique_symptoms, feature_columns