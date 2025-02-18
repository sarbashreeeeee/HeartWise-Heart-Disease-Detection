from flask import redirect, render_template, url_for
from app.blueprints.user_auth import user_auth_bp
from app.blueprints.user_auth.forms.register import RegisterForm


@user_auth_bp.route("/register", methods=["GET"])
def view_register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@user_auth_bp.route("/handleregister", methods=["POST"])
def handle_register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        full_name = register_form.full_name.data
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(f"khub garis {username}")

    else:
        print(register_form.errors)

    return redirect(url_for("user_auth.view_register"))
