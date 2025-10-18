import joblib
import os

print("🔍 Debugging model files...")

# Check if all required files exist
required_files = [
    "models/disease_model.pkl",
    "models/label_encoder.pkl", 
    "models/scaler.pkl",
    "models/unique_symptoms.pkl",
    "models/feature_columns.pkl"
]

for file in required_files:
    if os.path.exists(file):
        print(f"✅ {file} - EXISTS")
    else:
        print(f"❌ {file} - MISSING")

print("\n" + "="*50)

try:
    # Load and inspect saved components
    if os.path.exists("models/feature_columns.pkl"):
        feature_columns = joblib.load("models/feature_columns.pkl")
        print(f"📊 Feature columns ({len(feature_columns)}): {feature_columns[:5]}...")
    else:
        print("❌ feature_columns.pkl not found - need to retrain!")
        
    if os.path.exists("models/unique_symptoms.pkl"):
        unique_symptoms = joblib.load("models/unique_symptoms.pkl")
        print(f"💊 Unique symptoms ({len(unique_symptoms)}): {unique_symptoms[:5]}...")
    else:
        print("❌ unique_symptoms.pkl not found - need to retrain!")
        
    if os.path.exists("models/label_encoder.pkl"):
        label_encoder = joblib.load("models/label_encoder.pkl")
        print(f"🏥 Disease classes: {list(label_encoder.classes_)}")
    
except Exception as e:
    print(f"❌ Error loading files: {e}")
    print("🔄 You need to retrain the model with the updated code!")