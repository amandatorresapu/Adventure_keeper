from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import session, flash, redirect




class Adventure:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.id = data["id"]
        self.date = data["date"]
        self.location = data["location"]
        self.returntime = data["returntime"]
        self.emailkeeper = data["emailkeeper"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod 
    def create(cls,data):
        mysql = connectToMySQL("adventures_schema")
        query = "INSERT INTO adventures (user_id, date, location, returntime, emailkeeper) Values (%(user_id)s, %(date)s, %(location)s, %(returntime)s, %(emailkeeper)s);"
        
        user_id = mysql.query_db(query, data)

        return user_id

    @staticmethod
    def adventure_validator(data):
        is_valid = True

        if len(data["date"]) <= 1:
            flash("Date must be more than 1")
            is_valid = False

        if len(data["location"]) <= 4:
            flash("Location must be more than 4 charaters in length")
            is_valid = False

        if len(data["returntime"]) <= 3:
            flash("Time Return be more than 3 charaters in length")
            is_valid = False

        if len(data["emailkeeper"]) <= 1:
            flash("Email must be more than 1")
            is_valid = False
        return is_valid