from flask import jsonify, render_template, session
from flask_login import current_user, login_required
from app.blueprints.profile import profile_bp
from app.blueprints.profile.forms.profile_update import ProfileUpdateForm


@profile_bp.route("/", methods=["GET"])
@login_required
def view_profile_page():
    form = ProfileUpdateForm()

    return render_template("profile.html", form=form)


@profile_bp.route("/update_profile", methods=["POST"])
@login_required
def update_profile():
    form = ProfileUpdateForm()
    if form.validate_on_submit():
        print("Profile form validated!")
        try:

            current_user.full_name = (
                form.full_name.data if form.full_name.data else current_user.full_name
            )
            current_user.username = (
                form.username.data if form.username.data else current_user.username
            )
            current_user.email = (
                form.email.data if form.email.data else current_user.email
            )
            if (
                current_user.check_password(form.current_password.data)
                and form.new_password.data
            ):
                current_user.set_password(form.new_password.data)

                from app import db

                db.session.commit()

                print("Updated Successfully!")

                return jsonify(
                    {
                        "success": True,
                        "message": "Updated Successfully!",
                    }
                )

            print("Current Password does not match!")
            return jsonify(
                {
                    "success": False,
                    "message": "Current Password does not match!",
                }
            )
        except Exception as Ex:
            print("Error while updating!")
            return jsonify(
                {
                    "success": False,
                    "message": "Error while updating!",
                }
            )

    else:
        print(form.confirm_password.errors)
        print("Profile form not validated!")
        return jsonify(
            {
                "success": False,
                "message": "Profile Form Validation Failed!",
            }
        )
