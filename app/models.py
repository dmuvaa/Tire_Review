#!/usr/bin/python3

"""Import necessary modules"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='editor')  # default role is 'editor'

    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.Text)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Article {self.title}>'
