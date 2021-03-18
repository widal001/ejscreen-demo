from flask import Blueprint


webapp_bp = Blueprint("webapp", __name__)


@webapp_bp.route("/")
def home_page():
    return "Hello, World."
