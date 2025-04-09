from flask import jsonify, render_template
from flask_login import current_user, login_required
from sqlalchemy import desc
from app.blueprints.dashboard import dashboard_bp
from app.models.metric import Metric


@dashboard_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")


@dashboard_bp.route("/get_metrics", methods=["GET"])
@login_required
def get_metrics():
    try:
        data = Metric.query.filter_by(user_id=current_user.id)
        rows = []

        for row in data:
            print("Backend Timestamp:", row.timestamp)
            rows.append(
                {
                    "Total Cholesterol": row.cholesterol,
                    "Cigarettes Per Day": row.cigs_per_day,
                    "Systolic BP": row.sys_bp,
                    "Diastolic BP": row.dia_bp,
                    "BMI": row.bmi,
                    "Heart Rate": row.heart_rate,
                    "Blood Glucose": row.glucose,
                    "Date": row.timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                }
            )
        return jsonify(
            {
                "success": True,
                "message": "Successfully fetched metrics for dashboard!",
                "metrics": rows,
            }
        )
    except Exception as Ex:
        print("Error fetching metrics for dashboard!", Ex)
        return jsonify(
            {
                "success": False,
                "message": "Error fetching metrics for dashboard!",
            }
        )
