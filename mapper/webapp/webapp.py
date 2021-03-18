from flask import Blueprint, render_template

webapp_bp = Blueprint("webapp", __name__, template_folder="templates")


@webapp_bp.route("/")
def home_page():
    return render_template("index.html")
