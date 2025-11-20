from joblib import load
import pandas as pd
import numpy as np

model_under_25 = load("artifacts/model_under_25")
model_over_25 = load("artifacts/model_over_25")
scaler_under_25 = load("artifacts/scaler_under_25")
scaler_over_25 = load("artifacts/scaler_over_25")
model_col_under_25=load("artifacts/columns_under_25")
model_col_over_25=load("artifacts/columns_under_25")
scaler_model_over_25=scaler_over_25["scaler"]
scaler_model_under_25=scaler_under_25["scaler"]


insurance_plan_label={'Bronze': 1, 'Silver': 2, 'Gold': 3}

risk_scores = {
    "diabetes": 6,
    "heart disease": 8,
    "high blood pressure": 6,
    "thyroid": 5,
    "no disease": 0,
    "none": 0
}

categorical_cols = [
    "gender",
    "region",
    "marital_status",
    "bmi_category",
    "smoking_status",
    "employment_status",
    "medical_history"
]




def risk_factor(x):
    val=0
    for i in x.lower().split(" & "):
        val+=risk_scores[i]
    return val/14

def preprocessing_df(df):
    if df["age"].iloc[0] >25:
        df_over_25 = pd.DataFrame(np.zeros((1, len(model_col_over_25["columns"]))), columns=model_col_over_25["columns"])
        df_over_25[scaler_over_25['cols_to_scale']]=scaler_model_over_25.transform(df[scaler_over_25['cols_to_scale']])
        for col in categorical_cols:
            new_col = col + "_" + df[col].iloc[0]
            if new_col in df_over_25.columns:
                df_over_25[new_col]=1
        df_over_25["normalized_risk_factor"]=risk_factor(df["medical_history"].iloc[0])
        return df_over_25

    else:
        df_under_25 = pd.DataFrame(np.zeros((1, len(model_col_under_25["columns"]))), columns=model_col_under_25["columns"])
        df_under_25[scaler_under_25['cols_to_scale']] = scaler_model_under_25.transform(df[scaler_under_25['cols_to_scale']])
        for col in categorical_cols:
            new_col = col + "_" + df[col].iloc[0]
            if new_col in df_under_25.columns:
                df_under_25[new_col] = 1
        df_under_25["normalized_risk_factor"] = risk_factor(df["medical_history"].iloc[0])
        return df_under_25


def prediction(values):
    df=pd.DataFrame([values])
    df["insurance_plan"]=df["insurance_plan"].map(insurance_plan_label)
    if df["age"].iloc[0] > 25 :
        processed_df=preprocessing_df(df)
        processed_df.drop("income_level",axis=1,inplace=True)
        predict=model_over_25.predict(processed_df)
    else:
        processed_df=preprocessing_df(df)
        processed_df.drop("income_level",axis=1,inplace=True)
        predict=model_under_25.predict(processed_df)
    return round(predict[0])
