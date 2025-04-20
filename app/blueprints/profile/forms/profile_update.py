from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo


class ProfileUpdateForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            Optional(),
            Length(min=3, max=100, message="Name must be more than 3 characters!"),
        ],
    )
    username = StringField(
        "Username",
        validators=[
            Optional(),
            Length(min=3, max=100, message="Username must be more than 3 characters!"),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            Optional(),
            Email(message="Please enter a valid email!"),
        ],
    )
    current_password = PasswordField("Current Password", validators=[Optional()])
    new_password = PasswordField(
        "New Password",
        validators=[
            Optional(),
            Length(min=8, message="Password must be at least 8 characters long!"),
        ],
    )
    confirm_password = PasswordField(
        "Confirm New Password",
        validators=[
            Optional(),
            EqualTo("new_password", message="Passwords must match!"),
        ],
    )

    update = SubmitField("Update Profile")
