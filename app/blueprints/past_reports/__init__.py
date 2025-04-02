from flask import Blueprint

past_reports_bp = Blueprint(
    "past_reports",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/past-reports",
)
