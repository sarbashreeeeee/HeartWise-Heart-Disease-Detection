from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user
from app.blueprints.user_auth import user_auth_bp
from app.blueprints.user_auth.forms.login import LoginForm
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


@user_auth_bp.route("/login", methods=["GET"])
def view_login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    return render_template("login.html", form=form)


@user_auth_bp.route("/handlelogin", methods=["POST"])
def handle_login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash("Invalid Username!")
        elif user.password != password:
            flash("Invalid Password!")
        else:
            return redirect(url_for("main.index"))

    else:
        print(login_form.errors)

    return render_template("register.html", form=login_form)


@user_auth_bp.route("/logout")
@login_required
def logout():
    """Logs the user out."""
    logout_user()
    return redirect(url_for("auth.show_login"))


# User loader and Unauthorized handler
from app import login_manager
from app.models.user import User


@login_manager.user_loader
def load_user(user_id):
    """Checks if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirects unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("user_auth.view_login"))
