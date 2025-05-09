from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.blueprints.user_auth import user_auth_bp
from app.blueprints.user_auth.forms.login import LoginForm
from app.blueprints.user_auth.forms.register import RegisterForm
from app.models.user import User
from datetime import date


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
        username_exists = User.query.filter_by(
            username=register_form.username.data
        ).first()
        email_exists = User.query.filter_by(email=register_form.email.data).first()
        has_number = any(c.isdigit() for c in register_form.password.data)
        has_special = any(not c.isalnum() for c in register_form.password.data)
        has_upper = any(c.isupper() for c in register_form.password.data)
        has_lower = any(c.islower() for c in register_form.password.data)
        strong_password = has_number and has_special and has_lower and has_upper
        valid_dob = (
            True
            if (((date.today() - register_form.dob.data).days) / 365) >= 18
            else False
        )
        if username_exists:
            flash("Invalid Username.")
            return render_template("register.html", form=register_form)
        elif email_exists:
            flash("Invalid Email.")
            return render_template("register.html", form=register_form)
        elif not strong_password:
            flash("Weak Password.")
            return render_template("register.html", form=register_form)
        elif not valid_dob:
            flash("Invalid DOB.")
            return render_template("register.html", form=register_form)
        else:
            full_name = register_form.full_name.data
            username = register_form.username.data
            email = register_form.email.data
            password = register_form.password.data
            dob = register_form.dob.data
            gender = register_form.gender.data
            user = User(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
                dob=dob,
                gender=gender,
            )
            user.set_password(password)

            from app import db

            db.session.add(user)
            db.session.commit()  # Create new user
            return redirect(url_for("user_auth.view_login"))
    else:
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

    # Validate the login attempt
    if login_form.validate_on_submit():
        # print(login_form.username.data, login_form.password.data)
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))
        flash("Invalid username/password. Please enter valid Username and Password!")
        return redirect(url_for("user_auth.view_login"))
    else:
        print(login_form.errors)


@user_auth_bp.route("/logout")
@login_required
def logout():
    """Logs the user out."""
    logout_user()
    return redirect(url_for("user_auth.view_login"))


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
