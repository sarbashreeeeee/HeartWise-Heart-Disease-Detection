import pytest
from app.models.metric import Metric
from app.models.user import User
from datetime import date, datetime


@pytest.fixture
def test_user_model(db_session):
    user = User(
        full_name="Bahubali",
        dob=date(1990, 1, 1),
        gender="Male",
        username="bahu",
        email="bahubali@gmail.com",
        password="Bahubali@123",
    )
    db_session.add(user)
    db_session.commit()
    yield user
    db_session.delete(user)
    db_session.commit()


def test_metric_model(test_user_model):
    metric = Metric(
        gender="Male",
        age=35,
        current_smoker=False,
        cigs_per_day=0,
        bp_meds=False,
        prevalent_stroke=False,
        prevalent_hyp=False,
        diabetes=False,
        cholesterol=130,
        sys_bp=110,
        dia_bp=80,
        bmi=21,
        heart_rate=80,
        glucose=80,
        timestamp=datetime(2025, 1, 1, 11, 11, 11),
        prediction=False,
        height=2,
        weight=90,
        user_id=test_user_model.id,
    )
    assert metric.gender == "Male"
    assert metric.age == 35
    assert metric.current_smoker == False
    assert metric.cigs_per_day == 0
    assert metric.bp_meds == False
    assert metric.prevalent_stroke == False
    assert metric.prevalent_hyp == False
    assert metric.diabetes == False
    assert metric.cholesterol == 130
    assert metric.sys_bp == 110
    assert metric.dia_bp == 80
    assert metric.bmi == 21
    assert metric.heart_rate == 80
    assert metric.glucose == 80
    assert metric.timestamp == datetime(2025, 1, 1, 11, 11, 11)
    assert metric.prediction == False
    assert metric.height == 2
    assert metric.weight == 90
    assert metric.user_id == test_user_model.id
