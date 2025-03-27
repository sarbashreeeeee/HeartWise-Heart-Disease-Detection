from flask import jsonify, render_template
from flask_login import current_user, login_required
from app.blueprints.disease_detection import disease_detection_bp
from app.blueprints.disease_detection.forms.metrics_input import MetricsInputForm
from app.blueprints.disease_detection.services.detection_service import DetectionService
from app.models.metric import Metric


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
        try:
            print(form.gender.data)
            if form.cigarettes.data is None:
                form.cigarettes.data = 0
            metrics = Metric(
                gender=form.gender.data,
                age=int(form.age.data),
                current_smoker=int(form.smoker.data),
                cigs_per_day=int(form.cigarettes.data),
                bp_meds=int(form.bp_meds.data),
                prevalent_stroke=int(form.stroke.data),
                prevalent_hyp=int(form.hypertension.data),
                diabetes=int(form.diabetes.data),
                cholesterol=int(form.cholesterol.data),
                sys_bp=int(form.systolic.data),
                dia_bp=int(form.diastolic.data),
                bmi=int(form.bmi.data),
                heart_rate=int(form.heart_rate.data),
                glucose=int(form.glucose.data),
                user_id=current_user.id,
            )

            are_metrics_saved_to_db = DetectionService.save_metrics_to_db(metrics)
            if are_metrics_saved_to_db:
                pred_result = DetectionService.pred_disease(metrics)
                if pred_result == -1:
                    return jsonify(
                        {
                            "success": False,
                            "message": "Prediction Error!",
                        }
                    )
                return jsonify(
                    {
                        "success": True,
                        "message": f"Prediction Result: {pred_result}",
                    }
                )
            else:
                return jsonify(
                    {"success": False, "message": "Error saving metrics to DB!"}
                )
        except Exception as Ex:
            print(f"HYAAAAAAAAAA {Ex}")
            return jsonify({"success": False, "message": "Prediction Failed!"})

    else:
        print("Form Validation Failed!")
        return jsonify({"success": False, "message": "Form Validation Failed!"})
