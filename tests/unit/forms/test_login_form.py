from wtforms import PasswordField, StringField
from app.blueprints.user_auth.forms.login import LoginForm


def test_login_form(app):
    test_login_form = LoginForm()
    assert hasattr(test_login_form, "username")
    assert hasattr(test_login_form, "password")
    assert isinstance(test_login_form.username, StringField)
    assert isinstance(test_login_form.password, PasswordField)
