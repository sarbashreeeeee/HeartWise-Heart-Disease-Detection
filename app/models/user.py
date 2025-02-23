import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
from app import db


# User class
class User(UserMixin, db.Model):
    __tablename__ = "user"  # Name in db

    # UserID
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Full name
    full_name = db.Column(db.String(50), nullable=False)

    # Username
    username = db.Column(db.String(50), nullable=False, unique=True)

    # Email
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Password
    password = db.Column(db.String(300), nullable=False)
