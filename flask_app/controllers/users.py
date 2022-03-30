from flask import Flask, render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.adventure import Adventure

@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/login_page")
def display_login():

    return render_template("login.html")

@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/")

@app.route("/users/create", methods = ["POST"]) 
def create_user():
    if User.registry_validator(request.form):
        session["user_id"] = User.create(request.form)
    return redirect("/dashboard")

@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validator(request.form):
        flash("invalid login")
        return redirect("/")
    user = User.get_by_email(request.form)
    session["user_id"] = user.id

    return redirect("/dashboard")




