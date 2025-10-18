import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocess import preprocess_data

# Load dataset
print("📊 Loading dataset...")
data = pd.read_csv("data/animal_disease_dataset.csv")
print(f"Dataset shape: {data.shape}")

# Preprocess
print("🔄 Preprocessing data...")
df, label_encoder, scaler, unique_symptoms, feature_columns = preprocess_data(data)

X = df[feature_columns]  # Use specific column order
y = df['Disease']

print(f"Features shape: {X.shape}")
print(f"Number of classes: {len(label_encoder.classes_)}")

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
print("🤖 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# Evaluate model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# Save model and all necessary components
joblib.dump(model, "models/disease_model.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(unique_symptoms, "models/unique_symptoms.pkl")
joblib.dump(feature_columns, "models/feature_columns.pkl")

print("💾 Model and components saved successfully!")
print(f"📋 Available symptoms: {unique_symptoms}")
print(f"🏷️ Disease classes: {list(label_encoder.classes_)}")
print(f"🔧 Feature columns: {len(feature_columns)} features")