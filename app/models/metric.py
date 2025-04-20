import uuid
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app import db


# Metric class
class Metric(db.Model):
    __tablename__ = "metric"  # Name in db

    # MetricID
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Input Metrics
    gender = db.Column(db.Enum("Male", "Female", name="gender_enum"), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    current_smoker = db.Column(db.Boolean, nullable=False)
    cigs_per_day = db.Column(db.Integer, nullable=False)
    bp_meds = db.Column(db.Boolean, nullable=False)
    prevalent_stroke = db.Column(db.Boolean, nullable=False)
    prevalent_hyp = db.Column(db.Boolean, nullable=False)
    diabetes = db.Column(db.Boolean, nullable=False)
    cholesterol = db.Column(db.Integer, nullable=False)
    sys_bp = db.Column(db.Integer, nullable=False)
    dia_bp = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Integer, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    glucose = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(TIMESTAMP, nullable=False)
    prediction = db.Column(db.Boolean, nullable=True)
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)

    reports = db.relationship("Report", cascade="all, delete-orphan")

    # Setting user_id as foreign key
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
