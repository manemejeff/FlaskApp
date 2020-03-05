from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from theapp.myapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
