from wtforms import (
    DateField,
    DecimalField,
    IntegerField,
    PasswordField,
    RadioField,
    StringField,
)
from app.blueprints.profile.forms.profile_update import ProfileUpdateForm


def test_profile_update_form(app):
    test_profile_update_form = ProfileUpdateForm()
    assert hasattr(test_profile_update_form, "full_name")
    assert hasattr(test_profile_update_form, "username")
    assert hasattr(test_profile_update_form, "email")
    assert hasattr(test_profile_update_form, "current_password")
    assert hasattr(test_profile_update_form, "new_password")
    assert hasattr(test_profile_update_form, "confirm_password")

    assert isinstance(test_profile_update_form.full_name, StringField)
    assert isinstance(test_profile_update_form.username, StringField)
    assert isinstance(test_profile_update_form.email, StringField)
    assert isinstance(test_profile_update_form.current_password, PasswordField)
    assert isinstance(test_profile_update_form.new_password, PasswordField)
    assert isinstance(test_profile_update_form.confirm_password, PasswordField)
