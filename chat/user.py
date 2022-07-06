
from flask_login import UserMixin

from .db import get_db

class User(UserMixin):
    def __init__(self, _id, _name, _email, _profile_pic):
        self.id = _id
        self.name = _name
        self.email = _email
        self.profile_pic = _profile_pic

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(id, name, email, profile_pic):
        db = get_db()
        error=None
        try:
            db.execute(
                "INSERT INTO user (id, name, email, profile_pic) "
                "VALUES (?, ?, ?, ?)",
                (id, name, email, profile_pic),
            )
            db.commit()
        except:
            error="Insertion Falied"
        return error