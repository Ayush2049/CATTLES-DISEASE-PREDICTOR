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
## 📂 Project preview
## Disease Prediction Model Architecture

![Disease Prediction Model Architecture](https://github.com/Ayush2049/CATTLES-DISEASE-PREDICTOR/blob/0ad153e1e3bedd9be329aeb81a291f89ff2fb4ab/project-instances/disease-predicter.png)


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

## 📊 Dataset Format

Dataset link
https://www.kaggle.com/datasets/researcher1548/livestock-symptoms-and-diseases

CSV should have these columns:

| Column | Type | Example |
|--------|------|---------|
| `Animal` | string | "cow" |
| `Age` | integer | 5 |
| `Temperature` | float | 103.5 |
| `Symptoms` | string | "fever,cough" |
| `Disease` | string | "Pneumonia" |


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
