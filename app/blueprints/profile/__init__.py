from flask import Blueprint

profile_bp = Blueprint(
    "profile",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/profile",
)
