from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    full_name = StringField(
        "Full Name", validators=[DataRequired(message="Please enter your name!")]
    )
    username = StringField(
        "Username", validators=[DataRequired(message="Please enter your username!")]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Please enter your email!"),
            Email(message="PLease enter a valid email!"),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Please enter your password!")]
    )

    register_btn = SubmitField("Register")
