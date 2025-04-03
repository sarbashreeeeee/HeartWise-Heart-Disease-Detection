from flask import jsonify, redirect, render_template, request, url_for

from flask_login import current_user, login_required
from app.models.metric import Metric
from app.models.report import Report
from app.blueprints.past_reports import past_reports_bp


@past_reports_bp.route("/", methods=["GET"])
@login_required
def view_past_reports_list_page():
    reports = Report.query.order_by(Report.timestamp.desc()).all()
    return render_template("past_report_list.html", reports=reports)


@past_reports_bp.route("/past-report", methods=["GET"])
@login_required
def view_past_reports_page():
    try:
        report_id = request.args.get("report_id")
        report = Report.query.get(report_id)
        metric_id = report.metric_id
        metric = Metric.query.filter_by(id=metric_id).first()

        return render_template(
            "past_report.html",
            age=metric.age,
            gender=metric.gender,
            current_smoker="YES" if metric.current_smoker else "NO",
            cigs_per_day=metric.cigs_per_day,
            bp_meds="YES" if metric.bp_meds else "NO",
            prevalent_stroke="YES" if metric.prevalent_stroke else "NO",
            prevalent_hyp="YES" if metric.prevalent_hyp else "NO",
            diabetes="YES" if metric.diabetes else "NO",
            cholesterol=metric.cholesterol,
            sys_bp=metric.sys_bp,
            dia_bp=metric.dia_bp,
            bmi=metric.bmi,
            heart_rate=metric.heart_rate,
            glucose=metric.glucose,
            prediction=metric.prediction,
            report_id=report_id,
            timestamp=report.timestamp,
        )

    except Exception as Ex:
        print("Error while generating past report: ", Ex)
        return jsonify(
            {"success": False, "message": "Error while generating past report"}
        )
