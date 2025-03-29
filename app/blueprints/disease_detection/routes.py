from datetime import datetime
from flask import jsonify, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required
from app.blueprints.disease_detection import disease_detection_bp
from app.blueprints.disease_detection.forms.metrics_input import MetricsInputForm
from app.blueprints.disease_detection.services.detection_service import DetectionService
from app.models.metric import Metric
from app.models.report import Report


@disease_detection_bp.route("/", methods=["GET"])
@login_required
def view_metrics_input_page():
    form = MetricsInputForm()

    return render_template("metrics_input.html", form=form)


@disease_detection_bp.route("/report", methods=["GET"])
@login_required
def view_report_page():
    report_id = session.get("report_id") if session.get("report_id") else None
    metric_id = session.get("metric_id") if session.get("metric_id") else None
    report = Report.query.filter_by(id=report_id).first()
    metric = Metric.query.filter_by(id=metric_id).first()

    return render_template(
        "report.html",
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
        prediction=session.get("pred_result"),
        report_id=report_id,
        timestamp=report.timestamp,
    )


@disease_detection_bp.route("/make_prediction", methods=["POST"])
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

            pred_result = DetectionService.pred_disease(metrics)
            if pred_result == -1:
                return jsonify(
                    {
                        "success": False,
                        "message": "Prediction Error!",
                    }
                )
            else:
                metric_id = DetectionService.save_metrics_to_db(metrics)
                if metric_id == False or metric_id is None:
                    return jsonify(
                        {
                            "success": False,
                            "message": "Error saving data in the database!",
                        }
                    )
                session["metric_id"] = metric_id
                session["pred_result"] = int(pred_result)
                return jsonify(
                    {
                        "success": True,
                        "message": "Successfully saved metrics to Database!",
                    }
                )
        except Exception as Ex:
            print(f"Prediction Error {Ex}")
            return jsonify({"success": False, "message": "Prediction Failed!"})

    else:
        print("Form Validation Failed!")
        return jsonify({"success": False, "message": "Form Validation Failed!"})


@disease_detection_bp.route("/save_report_to_db", methods=["GET"])
@login_required
def save_report_to_db():
    try:
        # data = request.get_json()
        # print(data)
        metric_id = session.get("metric_id")
        print("report_id from session", metric_id)
        timestamp = datetime.now()
        report = Report(timestamp=timestamp, metric_id=metric_id)
        report_id = DetectionService.save_report_to_db(report)
        if not report_id:
            return jsonify(
                {
                    "success": False,
                    "message": "Report Not Saved!",
                }
            )
        else:
            session["report_id"] = report_id
            print("report_id from session", session.get("report_id"))
            return jsonify(
                {
                    "success": True,
                    "message": "Report Saved!",
                    "redirect": url_for("detect.view_report_page"),
                }
            )
    except Exception as Ex:
        print(f"Prediction Error {Ex}")
        return jsonify({"success": False, "message": "Prediction Failed!"})
