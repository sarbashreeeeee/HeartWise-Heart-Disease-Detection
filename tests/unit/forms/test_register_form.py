from wtforms import DateField, PasswordField, RadioField, StringField
from app.blueprints.user_auth.forms.register import RegisterForm
from datetime import date


def test_register_form(app):
    test_register_form = RegisterForm()
    assert hasattr(test_register_form, "dob")
    assert hasattr(test_register_form, "gender")
    assert hasattr(test_register_form, "full_name")
    assert hasattr(test_register_form, "username")
    assert hasattr(test_register_form, "email")
    assert hasattr(test_register_form, "password")

    assert isinstance(test_register_form.dob, DateField)
    assert isinstance(test_register_form.gender, RadioField)
    assert isinstance(test_register_form.full_name, StringField)
    assert isinstance(test_register_form.username, StringField)
    assert isinstance(test_register_form.email, StringField)
    assert isinstance(test_register_form.password, PasswordField)


def test_register_form_validation(app):
    test_register_form = RegisterForm(
        dob=date(1990, 11, 11),
        gender="Female",
        full_name="Rajmata Shivgami",
        username="ra",  # Usernmae must be of atleast 3 characters
        email="rajmata@gmail.com",
        password="Rajmata@123",
    )
    assert test_register_form.validate() == False
