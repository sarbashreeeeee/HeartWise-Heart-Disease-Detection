from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, RadioField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class MetricsInputForm(FlaskForm):
    # Height and Weight for BMI Calculator
    height = DecimalField(
        "Height (in meter)",
        validators=[
            Optional(),
            NumberRange(
                min=0.1,
                max=5,
                message="Please enter a valid height!",
            ),
        ],
    )

    weight = IntegerField(
        "Weight (in kg)",
        validators=[
            Optional(),
            NumberRange(
                min=1,
                max=300,
                message="Please enter a valid weight!",
            ),
        ],
    )

    # Lifestyle Factors
    smoker = RadioField(
        "Are you a current smoker?",
        choices=[(1, "Yes"), (0, "No")],
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
        "Are you currently taking any Blood Pressure medicines?",
        choices=[(1, "Yes"), (0, "No")],
        validators=[DataRequired()],
    )
    stroke = RadioField(
        "Do you have previous history of Stroke?",
        choices=[(1, "Yes"), (0, "No")],
        validators=[DataRequired()],
    )
    hypertension = RadioField(
        "Do you suffer from Hypertension?",
        choices=[(1, "Yes"), (0, "No")],
        validators=[DataRequired()],
    )
    diabetes = RadioField(
        "Do you have Diabetes?",
        choices=[(1, "Yes"), (0, "No")],
        validators=[DataRequired()],
    )

    # Current Health Metrics
    systolic = IntegerField(
        "Systolic Blood Pressure (mmHg)",
        validators=[
            DataRequired(),
            NumberRange(
                min=70,
                max=250,
                message="Systolic BP must be between 70 and 250 mmHg",
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
                message="Diastolic BP must be between 40 and 150 mmHg",
            ),
        ],
    )
    cholesterol = IntegerField(
        "Total Cholesterol (mg/dL)",
        validators=[
            DataRequired(),
            NumberRange(
                min=50,
                max=400,
                message="Cholesterol must be between 100 and 400 mg/dL",
            ),
        ],
    )
    glucose = IntegerField(
        "Blood Glucose (mg/dL)",
        validators=[
            DataRequired(),
            NumberRange(
                min=40,
                max=250,
                message="Blood glucose must be between 40 and 250 mg/dL",
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
                message="Heart rate must be between 40 and 200 bpm",
            ),
        ],
    )
    bmi = DecimalField(
        "BMI",
        validators=[
            DataRequired(),
            NumberRange(min=10, max=50, message="BMI must be between 10 and 50"),
        ],
    )

    # Submit button
    submit_btm = SubmitField("Assess My Heart Health")
