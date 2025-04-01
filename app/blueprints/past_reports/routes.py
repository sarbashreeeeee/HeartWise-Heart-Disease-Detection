from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required
from app.models.report import Report
from app.blueprints.past_reports import past_reports_bp

admin = Admin(template_mode="bootstrap3", name="Past Reports", url="/")

from app import db

admin.add_view(ModelView(Report, db.session))


@past_reports_bp.route("/", methods=["GET"])
@login_required
def view_past_reports_page():
    return admin.index()
