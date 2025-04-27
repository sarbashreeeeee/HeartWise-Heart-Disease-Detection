from app.models.metric import Metric
from app.models.user import User
from datetime import date


def test_user_model():
    user = User(
        full_name="Bahubali",
        dob=date(1990, 1, 1),
        gender="Male",
        username="bahu",
        email="bahubali@gmail.com",
        password="Bahubali@123",
    )
    assert user.full_name == "Bahubali"
    assert user.dob == date(1990, 1, 1)
    assert user.gender == "Male"
    assert user.username == "bahu"
    assert user.email == "bahubali@gmail.com"
    assert user.password == "Bahubali@123"
