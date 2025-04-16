import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


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

    # DOB
    dob = db.Column(db.Date, nullable=False)

    # Gender
    gender = db.Column(db.Enum("Male", "Female", name="gender_enum"), nullable=False)

    # Username
    username = db.Column(db.String(50), nullable=False, unique=True)

    # Email
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Password
    password = db.Column(db.String(300), nullable=False)

    metrics = db.relationship("Metric", cascade="all, delete-orphan")

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
