# PRODIGY_ML_01 – House Price Prediction in India

A modular machine learning pipeline to predict house prices using clean code, reproducible workflows, and deployable models. Built for clarity, scalability, and portfolio impact.

---

## Project Overview

This project uses housing data from India to train a regression model that predicts property prices based on key features. It emphasizes:

- 🔹 Modular code structure
- 🔹 Reproducible environment setup
- 🔹 Deployment-ready model via Streamlit
- 🔹 Clean repo hygiene for public sharing

---

## Files Included

| File
 Name   |
 | Description |

| `Notebook.ipynb` | Exploratory Data Analysis and initial modeling |

 | `House_Price_India.csv`| Dataset used for training and evaluation |
| `model.pkl`|
 Trained model saved in binary format (not editable in text editors)|

|  `app.py` | Streamlit app for interactive predictions|

| `requirements.txt`| Python dependencies for reproducibility|

| `.gitignore` |
Keeps repo clean by ignoring temp and system files |
|`LICENSE`|
MIT License for public use|

| `README.md`| Project overview and instructions|

---

## Getting Started

### Clone the Repository

```bash
git clone [def]
cd PRODIGY_ML_01
```

## Setup Environment
conda create -n prodigy_ml_01 python=3.10
conda activate prodigy_ml_01
pip install -r requirements.txt

## Launch App
streamlit run app.py

## Model Overview
- Type: [e.g., RandomForestClassifier]
- Training Data: [ Housing dataset with 10 features, sourced from Kaggle]
- Metrics: Accuracy: 92%, F1 Score: 0.89
- Saved as: `model.pkl` using joblib
- Preprocessing: StandardScaler applied to numeric features   
- **Used in**: `app.py` for real-time predictions via Streamlit interface  

## License
This project is licensed under the MIT `License`. See LICENSE for details.

## Acknowledgement
- Streamlit — for the app interface
- Pandas — for data manipulation
- Joblib — for model serialization
- [Your dataset source or inspiration] — e.g., Kaggle, UCI, or custom

[def]: https://github.com/Romeena7/PRODIGY_ML_01.git