# models.py
# Contains most of the configuration information
import os
from flask_sqlalchemy import SQLAlchemy

# Configuration
Db = SQLAlchemy()

class Users(Db.Model):
    __tablename__ = "minders"
    id = Db.Column(Db.Integer, primary_key=True)
    username = Db.Column(Db.String(64),
                            nullable=False,
                            unique=True,
                            index=True)
    password = Db.Column(Db.String, nullable=False)
    email = Db.Column(Db.String, nullable=False)
