from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.adventure import Adventure
from flask_app.models.user import User
#add session below function
@app.route("/dashboard")
def all_adventures_list():
    user=User.get_one({"id": session["user_id"]})
    
    return render_template("dashboard.html", user=user)

@app.route('/new_adventure')
def new_car():
    return render_template('new_adventure.html')




@app.route('/adventure/create', methods = ["POST"])
def create():
    if not Adventure.adventure_validator(request.form):
        return redirect("/new_adventure")
    Adventure.create(request.form)
    
    return redirect('/new_adventure')