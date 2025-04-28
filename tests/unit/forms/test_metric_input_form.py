from wtforms import (
    DateField,
    DecimalField,
    IntegerField,
    PasswordField,
    RadioField,
    StringField,
)
from app.blueprints.disease_detection.forms.metrics_input import MetricsInputForm


def test_metric_input_form(app):
    test_metric_input_form = MetricsInputForm()
    assert hasattr(test_metric_input_form, "height")
    assert hasattr(test_metric_input_form, "weight")
    assert hasattr(test_metric_input_form, "smoker")
    assert hasattr(test_metric_input_form, "cigarettes")
    assert hasattr(test_metric_input_form, "bp_meds")
    assert hasattr(test_metric_input_form, "stroke")
    assert hasattr(test_metric_input_form, "hypertension")
    assert hasattr(test_metric_input_form, "diabetes")
    assert hasattr(test_metric_input_form, "systolic")
    assert hasattr(test_metric_input_form, "diastolic")
    assert hasattr(test_metric_input_form, "cholesterol")
    assert hasattr(test_metric_input_form, "glucose")
    assert hasattr(test_metric_input_form, "heart_rate")
    assert hasattr(test_metric_input_form, "bmi")

    assert isinstance(test_metric_input_form.height, DecimalField)
    assert isinstance(test_metric_input_form.weight, IntegerField)
    assert isinstance(test_metric_input_form.smoker, RadioField)
    assert isinstance(test_metric_input_form.cigarettes, IntegerField)
    assert isinstance(test_metric_input_form.bp_meds, RadioField)
    assert isinstance(test_metric_input_form.stroke, RadioField)
    assert isinstance(test_metric_input_form.hypertension, RadioField)
    assert isinstance(test_metric_input_form.diabetes, RadioField)
    assert isinstance(test_metric_input_form.systolic, IntegerField)
    assert isinstance(test_metric_input_form.diastolic, IntegerField)
    assert isinstance(test_metric_input_form.cholesterol, IntegerField)
    assert isinstance(test_metric_input_form.glucose, IntegerField)
    assert isinstance(test_metric_input_form.bmi, DecimalField)


def test_metric_input_form_validation(app):
    test_metric_input_form = MetricsInputForm(
        height=2,
        weight=0,
        smoker=0,
        cigarettes=10,
        bp_meds=0,
        stroke=0,
        hypertension=0,
        diabetes=0,
        systolic=10,
        diastolic=80,
        cholesterol=130,
        glucose=90,
        heart_rate=80,
        bmi=20,
    )
    assert test_metric_input_form.validate() == False
