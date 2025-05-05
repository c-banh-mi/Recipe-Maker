#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
from app.models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists. Please choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already registered. Please choose a different one.")

class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=80)])
    description = TextAreaField("Description", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CommentForm(FlaskForm):
    body = TextAreaField("Comment", validators=[DataRequired()])
    parent_id = HiddenField()  # will be blank for top-level comments
    submit = SubmitField("Post Comment")

class RatingForm(FlaskForm):
    value = IntegerField(
        "Rating",
        validators=[DataRequired(), NumberRange(min=1, max=5)],
        description="1–5"
    )
    submit = SubmitField("Rate Comment")
