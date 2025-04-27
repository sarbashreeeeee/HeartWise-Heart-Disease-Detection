import pytest
from app.models.metric import Metric
from app.models.report import Report
from app.models.user import User
from datetime import date, datetime
from tests.unit.models.test_metric_model import test_user_model


@pytest.fixture
def test_metric_model(test_user_model, db_session):
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

    db_session.add(metric)
    db_session.commit()
    yield metric
    db_session.delete(metric)
    db_session.commit()


def test_report_model(test_metric_model):
    report = Report(
        timestamp=datetime(2025, 1, 1, 11, 11, 11),
        metric_id=test_metric_model.id,
    )

    assert report.timestamp == datetime(2025, 1, 1, 11, 11, 11)
    assert report.metric_id == test_metric_model.id
