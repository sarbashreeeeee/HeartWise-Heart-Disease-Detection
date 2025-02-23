from flask import redirect, render_template, url_for
from app.blueprints.user_auth import user_auth_bp
from app.blueprints.user_auth.forms.register import RegisterForm
from app.models.user import User


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
        # print(f"well done {username}")
        user = User(
            full_name=full_name, username=username, email=email, password=password
        )
        from app import db

        db.session.add(user)
        db.session.commit()
        return redirect("login.html")

    else:
        print(register_form.errors)

    return render_template("register.html", form=register_form)
