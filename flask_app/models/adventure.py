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
    def advent_get_all(cls):
        mysql = connectToMySQL("adventure_keeper_db")
        query = "SELECT * FROM adventures JOIN users on adventures.user_id = users.id;"
        results = mysql.query_db(query)
        if results:
            adventures = []
            for row in results:
                temp_adventure = cls(row)
                data = {
                    "id": row["users.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "email" : row["email"],
                    "password" : row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                    }
                temp_adventure.user = user.User(data)
                adventures.append(temp_adventure)
            return adventures    