from flask import jsonify, render_template, request, session
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
            if form.current_password.data:
                if current_user.check_password(form.current_password.data):
                    if form.new_password.data:
                        current_user.set_password(form.new_password.data)
                    else:
                        pass
                else:
                    print("Current Password does not match!")
                    return jsonify(
                        {
                            "success": False,
                            "message": "Current Password does not match!",
                        }
                    )
            # commit wala code hatau ani error case dekhau
            from app import db

            db.session.commit()

            print("Updated Successfully!")

            return jsonify(
                {
                    "success": True,
                    "message": "Updated Successfully!",
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


@profile_bp.route("/delete_profile", methods=["POST"])
@login_required
def delete_profile():
    try:
        password = request.get_json().get("password")
        print(password)
        if current_user.check_password(password):
            from app import db

            db.session.delete(current_user)
            db.session.commit()

            print("Profile Deleted Successfully!")
            return jsonify(
                {
                    "success": True,
                    "message": "Profile Deleted Successfully!",
                }
            )
        print("Incorrect Password!")
        return jsonify(
            {
                "success": False,
                "message": "Incorrect Password!",
            }
        )
    except Exception as Ex:
        print("An Unexpected Error Occurred when deleting user profile!", Ex)
        return jsonify(
            {
                "success": False,
                "message": "An Unexpected Error Occurred!",
            }
        )
