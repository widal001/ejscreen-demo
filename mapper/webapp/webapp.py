from flask import Blueprint, render_template
from datetime import datetime

webapp_bp = Blueprint("webapp", __name__, template_folder="templates")


@webapp_bp.context_processor
def inject_now():
    return {"now": datetime.utcnow()}


@webapp_bp.route("/")
def home_page():
    return render_template("index.html")
