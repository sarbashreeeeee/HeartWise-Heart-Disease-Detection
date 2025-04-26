from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    IntegerField,
    PasswordField,
    RadioField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    dob = DateField(
        "DOB",
        validators=[
            DataRequired(message="Please enter your Date of Birth!"),
        ],
    )
    gender = RadioField(
        "Gender",
        choices=[("Male", "Male"), ("Female", "Female")],
        validators=[DataRequired()],
    )
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(message="Please enter your name!"),
            Length(min=3, max=100, message="Name must be more than 3 characters!"),
        ],
    )
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Please enter your username!"),
            Length(min=3, max=100, message="Username must be more than 3 characters!"),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Please enter your email!"),
            Email(message="Please enter a valid email!"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Please enter your password!"),
            Length(min=8, message="Password must be at least 8 characters long!"),
        ],
    )

    register_btn = SubmitField("Register")
