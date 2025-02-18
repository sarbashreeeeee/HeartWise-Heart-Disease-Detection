from flask import Blueprint

user_auth_bp = Blueprint(
    "user_auth", __name__, template_folder="templates", url_prefix="/auth"
)
