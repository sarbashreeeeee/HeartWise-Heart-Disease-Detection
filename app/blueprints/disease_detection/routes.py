from flask import render_template
from flask_login import login_required
from app.blueprints.disease_detection import disease_detection_bp


@disease_detection_bp.route("/", methods=["GET"])
@login_required
def view_metrics_input_page():
    return render_template("metrics_input.html")
