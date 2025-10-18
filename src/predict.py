import pandas as pd
import joblib
import numpy as np

# Load model and all components
model = joblib.load("models/disease_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
scaler = joblib.load("models/scaler.pkl")
unique_symptoms = joblib.load("models/unique_symptoms.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

def predict_disease(animal, age, temperature, symptoms):
    """
    Predict disease based on animal info and symptoms
    
    Args:
        animal (str): Type of animal (cow, buffalo, sheep, goat)
        age (int): Age of animal
        temperature (float): Temperature in Fahrenheit
        symptoms (list): List of symptoms
    
    Returns:
        tuple: (disease_name, confidence, valid_symptoms)
    """
    
    # Clean and validate symptoms
    symptoms = [s.strip().lower() for s in symptoms]
    valid_symptoms = [s for s in symptoms if s in unique_symptoms]
    
    if len(valid_symptoms) == 0:
        print(f"⚠️ Warning: No valid symptoms found. Available symptoms: {unique_symptoms}")
    
    # Initialize feature vector with zeros
    feature_dict = {}
    
    # Add symptom features
    for symptom in unique_symptoms:
        feature_dict[symptom] = 1 if symptom in valid_symptoms else 0
    
    # Add animal type features (one-hot encoded)
    animals = ['buffalo', 'cow', 'goat', 'sheep']
    for animal_type in animals:
        feature_dict[f'Animal_{animal_type}'] = 1 if animal.lower() == animal_type else 0
    
    # Add numerical features (will be scaled later)
    feature_dict['Age'] = age
    feature_dict['Temperature'] = temperature
    
    # Create DataFrame with exact feature order from training
    row_df = pd.DataFrame([feature_dict])
    
    # Ensure we have all required columns in correct order
    row_df = row_df.reindex(columns=feature_columns, fill_value=0)
    
    # Scale numerical features
    numerical_cols = ['Age', 'Temperature']
    row_df[numerical_cols] = scaler.transform(row_df[numerical_cols])
    
    # Make prediction
    prediction_proba = model.predict_proba(row_df)[0]
    prediction = model.predict(row_df)[0]
    confidence = max(prediction_proba)
    
    # Convert prediction back to disease name
    disease = label_encoder.inverse_transform([prediction])[0]
    
    return disease, confidence, valid_symptoms

def get_available_info():
    """Return available symptoms and animals for reference"""
    return {
        'symptoms': unique_symptoms,
        'animals': ['cow', 'buffalo', 'sheep', 'goat'],
        'diseases': list(label_encoder.classes_)
    }