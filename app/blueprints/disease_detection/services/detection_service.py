from datetime import datetime
import os
import pandas as pd
from flask import current_app
from joblib import load
import traceback
import xgboost

from app.models.metric import Metric
from app.models.report import Report


class DetectionService:
    model_directory = current_app.config["ML_MODEL_FOLDER"]
    disease_pred_model = load(os.path.join(model_directory, "PredModel.joblib"))

    @staticmethod
    def pred_disease(metrics):
        """metrics parameter is an object of the class metric.py"""
        try:
            df = DetectionService.map_column_names(metrics)
            pred = DetectionService.disease_pred_model.predict(df)[0]
            print(pred)
            return pred
        except Exception as Ex:
            print(f"Exception when predicting disease{Ex}")
            print(traceback.format_exc())
            return -1

    @staticmethod
    def map_column_names(metrics):
        # Mapping dictionary to translate input metrics to dataset column names
        dataset_col_names = {
            "male": metrics.gender,
            "age": metrics.age,
            "currentSmoker": metrics.current_smoker,
            "cigsPerDay": metrics.cigs_per_day,
            "BPMeds": metrics.bp_meds,
            "prevalentStroke": metrics.prevalent_stroke,
            "prevalentHyp": metrics.prevalent_hyp,
            "diabetes": metrics.diabetes,
            "totChol": metrics.cholesterol,
            "sysBP": metrics.sys_bp,
            "diaBP": metrics.dia_bp,
            "BMI": metrics.bmi,
            "heartRate": metrics.heart_rate,
            "glucose": metrics.glucose,
        }
        df = pd.DataFrame([dataset_col_names])

        # Handle value transformations
        # Convert categorical variables
        df["male"] = (df["male"] == "Male").astype(int)
        df["currentSmoker"] = (df["currentSmoker"] == "yes").astype(int)
        df["BPMeds"] = (df["BPMeds"] == "yes").astype(int)
        df["prevalentStroke"] = (df["prevalentStroke"] == "yes").astype(int)
        df["prevalentHyp"] = (df["prevalentHyp"] == "yes").astype(int)
        df["diabetes"] = (df["diabetes"] == "yes").astype(int)

        # df = df.drop("_sa_instance_state", axis=1)
        return df

    @staticmethod
    def save_metrics_to_db(metrics):
        try:
            from app import db

            db.session.add(metrics)
            db.session.commit()
            return metrics.id

        except Exception as Ex:
            print(f"Error saving metrics to database: {Ex}")
            return False

    @staticmethod
    def save_report_to_db(report):
        try:
            from app import db

            db.session.add(report)
            db.session.commit()
            return report.id

        except Exception as Ex:
            print(f"Error saving report to database: {Ex}")
            return False

    @staticmethod
    def save_pred_to_db(metric_id, pred_result):
        try:
            from app import db

            db.session.query(Metric).filter_by(id=metric_id).update(
                {"prediction": pred_result}
            )
            db.session.commit()
            return True
        except Exception as Ex:
            print(f"Error saving prediction to database: {Ex}")
            return False
