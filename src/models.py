from sqlalchemy.orm import relationship, backref

from src.db import db


class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    # hash = db.Column(db.String(255), nullable=False)
    # token_cookie = db.Column(db.String(255), nullable=True, default=None)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=True)
    birth = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'User({self.username}, {self.email})'

    def __str__(self):
        return f'{self.username}'
