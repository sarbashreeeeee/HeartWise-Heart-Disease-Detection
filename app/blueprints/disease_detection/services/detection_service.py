import os
import pandas as pd
from flask import current_app
from joblib import load


class DetectionService:
    model_directory = current_app.config["ML_MODEL_FOLDER"]
    disease_pred_model = load(os.path.join(model_directory, "LRModel.joblib"))

    # This is just here for referencing
    dataset_col_names = [
        "male",
        "age",
        "currentSmoker",
        "cigsPerDay",
        "BPMeds",
        "prevalentStroke",
        "prevalentHyp",
        "diabetes",
        "totChol",
        "sysBP",
        "diaBP",
        "BMI",
        "heartRate",
        "glucose",
        "TenYearCHD",
    ]

    @staticmethod
    def pred_disease(metrics):
        """metrics parameter is an object of the class metric.py"""
        try:
            print("JPT 1")
            # are_metrics_saved_to_db = DetectionService.save_metrics_to_db(metrics)
            # if are_metrics_saved_to_db:
            metric_dict = vars(metrics)
            print("JPT 2", [metric_dict.keys()])
            # print("Metric dict gender", metric_dict["gender"])
            df = pd.DataFrame([metric_dict])
            print(df.columns)
            print(df)
            df = DetectionService.map_column_names(df)
            pred = DetectionService.disease_pred_model.predict(df)
            print(pred)
            return pred
            # return -1
        except Exception as Ex:
            print(f"Exception when predicting disease{Ex}")
            return -1

    @staticmethod
    def map_column_names(df):
        # Mapping dictionary to translate input metrics to dataset column names
        column_mapping = {
            "gender": "male",
            "current_smoker": "currentSmoker",
            "cigs_per_day": "cigsPerDay",
            "bp_meds": "BPMeds",
            "prevalent_stroke": "prevalentStroke",
            "prevalent_hyp": "prevalentHyp",
            "cholesterol": "totChol",
            "sys_bp": "sysBP",
            "dia_bp": "diaBP",
            "heart_rate": "heartRate",
            "bmi": "BMI",
            "age": "age",
            "glucose": "glucose",
        }

        # Rename columns using the mapping
        df = df.rename(columns=column_mapping)

        # Handle value transformations
        # Convert categorical variables
        df["male"] = (df["male"] == "Male").astype(int)
        df["currentSmoker"] = (df["currentSmoker"] == "yes").astype(int)
        df["BPMeds"] = (df["BPMeds"] == "yes").astype(int)
        df["prevalentStroke"] = (df["prevalentStroke"] == "yes").astype(int)
        df["prevalentHyp"] = (df["prevalentHyp"] == "yes").astype(int)
        df["diabetes"] = (df["diabetes"] == "yes").astype(int)

        df = df.drop("_sa_instance_state", axis=1)
        return df

    @staticmethod
    def save_metrics_to_db(metrics):
        try:
            from app import db

            db.session.add(metrics)
            db.session.commit()
            return True

        except Exception as Ex:
            print(f"Error saving metrics to database: {Ex}")
            return False
