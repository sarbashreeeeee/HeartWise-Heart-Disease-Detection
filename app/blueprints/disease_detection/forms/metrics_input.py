from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class MetricsInputForm(FlaskForm):
    # Personal Information
    age = IntegerField(
        "Age",
        validators=[
            DataRequired(),
            NumberRange(min=18, max=120, message="Age must be between 18 and 120."),
        ],
    )
    gender = RadioField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
    )

    # Lifestyle Factors
    smoker = RadioField(
        "Current Smoker?",
        choices=[("yes", "Yes"), ("no", "No")],
        validators=[DataRequired()],
    )
    cigarettes = IntegerField(
        "Cigarettes per day",
        validators=[
            Optional(),
            NumberRange(
                min=1,
                max=100,
                message="Please enter a valid number of cigarettes (1-100)",
            ),
        ],
    )

    # Medical History
    bp_meds = RadioField(
        "Taking BP Medicines?",
        choices=[("yes", "Yes"), ("no", "No")],
        validators=[DataRequired()],
    )
    stroke = RadioField(
        "Previous Stroke History?",
        choices=[("yes", "Yes"), ("no", "No")],
        validators=[DataRequired()],
    )
    hypertension = RadioField(
        "Hypertension?",
        choices=[("yes", "Yes"), ("no", "No")],
        validators=[DataRequired()],
    )
    diabetes = RadioField(
        "Diabetes?", choices=[("yes", "Yes"), ("no", "No")], validators=[DataRequired()]
    )

    # Current Health Metrics
    systolic = IntegerField(
        "Systolic Blood Pressure (mmHg)",
        validators=[
            DataRequired(),
            NumberRange(
                min=70,
                max=250,
                message="Systolic BP must be between 70 and 250 mmHg",  # yet to verify
            ),
        ],
    )
    diastolic = IntegerField(
        "Diastolic Blood Pressure (mmHg)",
        validators=[
            DataRequired(),
            NumberRange(
                min=40,
                max=150,
                message="Diastolic BP must be between 40 and 150 mmHg",  # yet to verify
            ),
        ],
    )
    cholesterol = IntegerField(
        "Total Cholesterol (mg/dL)",
        validators=[
            DataRequired(),
            NumberRange(
                min=100,
                max=600,
                message="Cholesterol must be between 100 and 600 mg/dL",  # yet to verify
            ),
        ],
    )
    glucose = IntegerField(
        "Blood Glucose (mg/dL)",
        validators=[
            DataRequired(),
            NumberRange(
                min=40,
                max=400,
                message="Blood glucose must be between 40 and 400 mg/dL",  # yet to verify
            ),
        ],
    )
    heart_rate = IntegerField(
        "Heart Rate (bpm)",
        validators=[
            DataRequired(),
            NumberRange(
                min=40,
                max=200,
                message="Heart rate must be between 40 and 200 bpm",  # yet to verify
            ),
        ],
    )
    bmi = FloatField(
        "BMI",
        validators=[
            DataRequired(),
            NumberRange(min=10, max=50, message="BMI must be between 10 and 50"),
        ],
    )

    # Submit button
    submit_btm = SubmitField("Assess My Heart Health")
