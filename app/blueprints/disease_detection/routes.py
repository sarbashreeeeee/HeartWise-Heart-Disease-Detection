from flask import jsonify, render_template
from flask_login import login_required
from app.blueprints.disease_detection import disease_detection_bp
from app.blueprints.disease_detection.forms.metrics_input import MetricsInputForm


@disease_detection_bp.route("/", methods=["GET"])
@login_required
def view_metrics_input_page():
    form = MetricsInputForm()

    return render_template("metrics_input.html", form=form)


@disease_detection_bp.route("make_prediction", methods=["POST"])
@login_required
def make_disease_pred():
    form = MetricsInputForm()
    if form.validate_on_submit():
        return jsonify(
            {
                "success": True,
                "message": f"Value of Cigarettes per day: {form.cigarettes.data}",
            }
        )
    else:
        print("form validate chaina")
        return jsonify({"success": False, "message": "k"})
