from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.blueprints.user_auth import user_auth_bp
from app.blueprints.user_auth.forms.login import LoginForm
from app.blueprints.user_auth.forms.register import RegisterForm
from app.models.user import User


@user_auth_bp.route("/register", methods=["GET"])
def view_register():
    """User register page.
    GET requests serve sign-up page."""
    form = RegisterForm()
    return render_template("register.html", form=form)


@user_auth_bp.route("/handleregister", methods=["POST"])
def handle_register():
    """POST requests validate form & user creation."""
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
        db.session.commit()  # Create new user
        return redirect(url_for("user_auth.view_login"))

    else:
        print(register_form.errors)

    return render_template("register.html", form=register_form)


# psd hash yet to implement for register


@user_auth_bp.route("/login", methods=["GET"])
def view_login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    return render_template("login.html", form=form)


@user_auth_bp.route("/handlelogin", methods=["POST"])
def handle_login():
    login_form = LoginForm()

    # Validate the login attempt
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.password == login_form.password.data:
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))
        flash("Invalid username/password combination")
        return render_template("login.html", form=login_form)

    else:
        print(login_form.errors)


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
