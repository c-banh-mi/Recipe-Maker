#models.py
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    display_name = sa.Column(sa.String(64), nullable=True) 
    username = sa.Column(sa.String(64), index=True, unique=True, nullable=False)
    email = sa.Column(sa.String(120), index=True, unique=True, nullable=False)
    password_hash = sa.Column(sa.String(256), nullable=False)
    recipes = so.relationship("Recipe", backref="author", lazy=True)
    comments = so.relationship('Comment', backref='author', lazy=True)
    ratings = so.relationship('CommentRating', backref='rater', lazy=True)
    favorites = so.relationship('Favorite', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username!r}>"

    def has_favorited(self, recipe):
        return Favorite.query.filter_by(user_id=self.id, recipe_id=recipe.id).first() is not None

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
    comments = so.relationship('Comment', backref='recipe', lazy=True)
    favorites = so.relationship('Favorite', backref='recipe', lazy='dynamic')

    def __repr__(self):
        return f"<Recipe {self.title}>"
    
class Comment(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    recipe_id = sa.Column(sa.Integer, sa.ForeignKey('recipe.id'), nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey('comment.id'), nullable=True)
    replies = so.relationship('Comment', backref=so.backref('parent', remote_side=[id]), lazy=True)
    ratings = so.relationship('CommentRating', backref='comment', lazy=True, cascade='all, delete')

class CommentRating(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    comment_id = sa.Column(sa.Integer, sa.ForeignKey('comment.id'), nullable=False)
    value = sa.Column(sa.Integer, nullable=False)  # e.g., 1-5 or +1/-1
    __table_args__ = (
        sa.UniqueConstraint('user_id', 'comment_id', name='uix_user_comment'),
    )

class Favorite(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    recipe_id = sa.Column(sa.Integer, sa.ForeignKey('recipe.id'), nullable=False)
    __table_args__ = (
        sa.UniqueConstraint('user_id', 'recipe_id', name='uix_user_recipe_favorite'),
    )
