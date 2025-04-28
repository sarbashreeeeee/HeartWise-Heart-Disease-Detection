from app.blueprints.disease_detection.services.detection_service import DetectionService
from app.models.metric import Metric
from app.models.report import Report
from app.models.user import User
from datetime import date, datetime
from tests.unit.models.test_report_model import test_metric_model
from tests.unit.models.test_metric_model import test_user_model
import pandas as pd


def test_map_column_names(test_metric_model):
    test_result = DetectionService.map_column_names(test_metric_model)
    # Check if returned object is a DataFrame
    assert isinstance(test_result, pd.DataFrame)

    # Check if all expected columns are present
    expected_columns = [
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
    ]
    assert list(test_result) == expected_columns

    # Check if transformations happened correctly
    assert test_result["male"][0] == 1
    assert test_result["currentSmoker"][0] == 0
    assert test_result["BPMeds"][0] == 0
    assert test_result["prevalentStroke"][0] == 0
    assert test_result["prevalentHyp"][0] == 0
    assert test_result["diabetes"][0] == 0

    # Check if numerical values are mapped correctly
    assert test_result["age"][0] == 35
    assert test_result["cigsPerDay"][0] == 0
    assert test_result["totChol"][0] == 130
    assert test_result["sysBP"][0] == 110
    assert test_result["diaBP"][0] == 80
    assert test_result["BMI"][0] == 21
    assert test_result["heartRate"][0] == 80
    assert test_result["glucose"][0] == 80


def test_save_metrics_to_db(test_metric_model):
    test_result = DetectionService.save_metrics_to_db(test_metric_model)
    assert test_result == test_metric_model.id


def test_save_report_to_db(test_metric_model):
    report = Report(
        timestamp=datetime(1990, 11, 11, 11, 11, 11), metric_id=test_metric_model.id
    )
    test_result = DetectionService.save_report_to_db(report)
    assert test_result == report.id


def test_save_pred_to_db(test_metric_model):
    test_result = DetectionService.save_pred_to_db(
        metric_id=test_metric_model.id, pred_result=0
    )
    assert test_result == True
