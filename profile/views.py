from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_app = Blueprint("profile_app", __name__)


@profile_app.route("/profile")
@login_required
def profile():
    return render_template("/profile/profile.html", current_user=current_user)
