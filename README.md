# Health Premium Prediction

This project predicts the annual health insurance premium for an individual using a Machine Learning model and a Streamlit web app. User inputs (age, gender, BMI category, smoking status, region, income, employment type, medical history, etc.) are preprocessed and passed to a trained model to return an estimated premium. Two separate models are used for users under 25 and for users 25 or older.

---

## Project Workflow

1. User inputs collected from Streamlit UI  
2. Inputs converted into a DataFrame  
3. Age-based model selection (under_25 or over_25)  
4. Numerical features scaled using pre-trained scalers  
5. Categorical features one-hot encoded  
6. Column alignment applied to match training schema  
7. Prediction returned by the appropriate ML model

---

## Machine Learning (Brief)

- Data cleaning and preprocessing  
- Univariate and bivariate analysis for feature insight  
- One-hot encoding for categorical variables  
- StandardScaler applied to numerical features  
- Trained two regression models: `model_under_25` and `model_over_25`  
- Hyperparameter tuning and selection based on MAE/RMSE/R²  
- Saved models, scalers, and training column structures for inference

---

## Repository Structure

```plaintext
Health-Premium-Prediction/
│
├── main.py
├── make_prediction.py
├── requirements.txt
│
├── artifacts/
│   ├── model_over_25
│   ├── model_under_25
│   ├── columns_over_25
│   ├── columns_under_25
│   ├── scaler_over_25
│   ├── scaler_under_25
│
└── README.md
```
---

## How to Run

Install dependencies:

    pip install -r requirements.txt

Run the Streamlit application:

    streamlit run main.py

---

## Notes

- The `artifacts/` folder contains all trained models, scalers, and column definitions.  
- The prediction logic inside `make_prediction.py` ensures the input data is processed exactly the same way as it was during training (scaling, encoding, and column alignment).

---
