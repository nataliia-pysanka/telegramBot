import bcrypt
from src.db import db
from src.models import User


def create_user(name: str, email: str, password: str):
    """
    Method will create new record in the user table
    """
    hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(
        rounds=10))
    hashed = hash_pass.decode('utf-8')

    user = User(username=name, email=email, hash=hashed)
    db.session.add(user)
    db.session.commit()
    return user


def login(email: str, password: str):
    """
    Method will return user object if it exists and
    inputted password was correct
    """
    user = get_user_by_email(email)
    if not user:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), user.hash.encode('utf-8')):
        return None
    return user


def get_user_by_email(email: str):
    """
    Method will return user object by its email
    """
    user = db.session.query(User).filter(User.email == email).\
        first()
    return user


def get_user_by_id(ids: int):
    """
    Method will return user object by its id
    """
    user = db.session.query(User).filter(User.id == ids).\
        first()
    return user


def set_token(user: User, token: str):
    """
    Method will create token for current user
    """
    user.token_cookie = token
    db.session.commit()


def get_user_by_token(token):
    """
    Method will return user by token
    """
    user = db.session.query(User).filter(User.token_cookie == token).first()
    if not user:
        return None
    return user
