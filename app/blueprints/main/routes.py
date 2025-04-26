from flask import render_template
from flask_login import login_required
from app.blueprints.main import main_bp


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")
