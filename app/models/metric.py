import uuid
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

    # Metric name
    metric_name = db.Column(db.String(50), nullable=False, unique=True)

    # Metric tupe
    metric_type = db.Column(db.String(50), nullable=False, unique=True)

    # Values
    email = db.Column(db.Integer(100), nullable=False, unique=True)
