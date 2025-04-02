from flask import redirect, render_template, url_for

from flask_login import current_user, login_required
from app.models.metric import Metric
from app.models.report import Report
from app.blueprints.past_reports import past_reports_bp


@past_reports_bp.route("/", methods=["GET"])
@login_required
def view_past_reports_page():

    reports = Report.query.join(Metric).filter(Metric.user_id == current_user.id).all()
    return render_template("past_reports.html", reports=reports)
