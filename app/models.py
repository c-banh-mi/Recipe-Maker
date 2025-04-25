#models.py
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(64), index=True, unique=True, nullable=False)
    email = sa.Column(sa.String(120), index=True, unique=True, nullable=False)
    password_hash = sa.Column(sa.String(256), nullable=False)
    recipes = so.relationship("Recipe", backref="author", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username!r}>"

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Recipe(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(80), nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    ingredients = sa.Column(sa.Text, nullable=False)
    instructions = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.title}>"
