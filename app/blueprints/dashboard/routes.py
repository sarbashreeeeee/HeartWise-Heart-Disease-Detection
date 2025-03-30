from flask import render_template
from flask_login import login_required
from app.blueprints.dashboard import dashboard_bp


@dashboard_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")
