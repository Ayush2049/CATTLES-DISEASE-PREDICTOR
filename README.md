# 🐄 Animal Disease Prediction System

> Machine Learning system for predicting livestock diseases using symptoms, age, and temperature

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

---

## 🎯 Overview

A **Random Forest Classifier** that predicts diseases in livestock (cows, buffaloes, sheep, goats) based on clinical symptoms, age, and body temperature with ~95% accuracy.

**Supported Animals:** 🐄 Cow | 🐃 Buffalo | 🐑 Sheep | 🐐 Goat

---

## ✨ Key Features

- 🤖 Random Forest Classifier with 95% accuracy
- 🔬 Multi-symptom analysis with confidence scoring
- 🌡️ Temperature & age-based diagnosis
- 💾 Persistent model storage with joblib
- ✅ Automatic symptom validation

---

## 📂 Project Structure
```
ANIMAL-DISEASE-PREDICTION/
├── data/
│   └── animal_disease_dataset.csv
├── models/
│   ├── disease_model.pkl
│   ├── label_encoder.pkl
│   ├── scaler.pkl
│   ├── unique_symptoms.pkl
│   └── feature_columns.pkl
├── train_model.py
├── preprocess.py
├── predict.py
└── requirements.txt
```

---

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/animal-disease-prediction.git
cd animal-disease-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
```txt
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
joblib>=1.0.0
```

---

## 🎓 Training the Model
```bash
python train_model.py
```

**Output:**
```
📊 Loading dataset...
Dataset shape: (1500, 5)
🔄 Preprocessing data...
Features shape: (1500, 45)
🤖 Training Random Forest model...
✅ Model Accuracy: 0.95
💾 Model and components saved successfully!
```

---

## 🔮 Making Predictions

### Python Usage
```python
from predict import predict_disease, get_available_info

# Predict disease
disease, confidence, valid_symptoms = predict_disease(
    animal="cow",
    age=5,
    temperature=103.5,
    symptoms=["fever", "cough", "lethargy"]
)

print(f"Disease: {disease}")
print(f"Confidence: {confidence:.2%}")
print(f"Valid Symptoms: {valid_symptoms}")
```

### Get Available Options
```python
info = get_available_info()
print("Animals:", info['animals'])
print("Symptoms:", info['symptoms'])
print("Diseases:", info['diseases'])
```

---

## 📊 Dataset Format

Your CSV should have these columns:

| Column | Type | Example |
|--------|------|---------|
| `Animal` | string | "cow" |
| `Age` | integer | 5 |
| `Temperature` | float | 103.5 |
| `Symptoms` | string | "fever,cough" |
| `Disease` | string | "Pneumonia" |

**Sample CSV:**
```csv
Animal,Age,Temperature,Symptoms,Disease
cow,5,103.2,"fever,cough,lethargy",Pneumonia
buffalo,7,102.8,"reduced appetite,diarrhea",Enteritis
sheep,2,104.5,"lameness,mouth lesions,fever",FMD
goat,3,101.5,"bloating,loss of appetite",Bloat
```

---

## 🔄 How It Works
```
Input (animal, age, temp, symptoms)
         ↓
Symptom Validation
         ↓
Feature Engineering (one-hot + scaling)
         ↓
Random Forest Prediction
         ↓
Output (disease, confidence, valid symptoms)
```

---

## 📋 Example Use Cases

**Dairy Cow Health Check:**
```python
predict_disease("cow", 6, 102.8, ["fever", "swollen udder"])
# Result: Mastitis
```

**Sheep Flock Screening:**
```python
predict_disease("sheep", 2, 104.2, ["lameness", "mouth lesions", "fever"])
# Result: Foot-and-Mouth Disease (FMD)
```

---

## ⚠️ Important Notes

- Temperature must be in Fahrenheit
- Age in years (integer)
- Symptom names are case-insensitive
- **Always verify predictions with a licensed veterinarian**
- This tool assists diagnosis, does not replace professional care

---



## 👨‍💻 Author

**Ayush Sharma**

- 📧 Email: [dm.ayushsharma@gmail.com](mailto:dm.ayushsharma@gmail.com)
- 🐙 GitHub: [@Ayush2049](https://github.com/Ayush2049)
- 💼 LinkedIn: [Ayush Sharma](https://in.linkedin.com/in/ayush-sharma-8805842ba)

---


---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ for animal welfare

</div>
