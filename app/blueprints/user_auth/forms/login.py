from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    username = StringField(
        "Username", validators=[DataRequired(message="Please enter your username!")]
    )

    password = PasswordField(
        "Password", validators=[DataRequired(message="Please enter your password!")]
    )

    register_btn = SubmitField("Register")
