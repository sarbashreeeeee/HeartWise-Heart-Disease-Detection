import uuid
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app import db


# Report class
class Report(db.Model):
    __tablename__ = "report"  # Name in db

    # ReportID
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Other Columns
    timestamp = db.Column(TIMESTAMP, nullable=False)

    # Setting metric_id as foreign key
    metric_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("metric.id"), nullable=False
    )
    metric = db.relationship("Metric")
