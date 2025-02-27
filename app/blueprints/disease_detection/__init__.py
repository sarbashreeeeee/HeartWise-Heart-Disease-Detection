from flask import Blueprint

disease_detection_bp = Blueprint(
    "detect",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/heart-disease-detection",
)
