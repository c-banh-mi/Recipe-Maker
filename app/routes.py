# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm, RegistrationForm, RecipeForm, CommentForm, RatingForm, EditProfileForm
from app.models import User, Recipe, Comment, CommentRating, Favorite
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
import sqlalchemy as sa
from datetime import datetime
import zoneinfo

main = Blueprint("main", __name__)

@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.recipes"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.recipes"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("main.login"))
        login_user(user)
        return redirect(url_for("main.recipes"))
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/recipes")
@login_required
def recipes():
    tag = request.args.get("tag", "")
    all_recipes = Recipe.query

    if tag:
        all_recipes = all_recipes.filter(Recipe.tags.ilike(f"%{tag}%"))

    recipes = all_recipes.all()

    all_tags = set()
    for r in Recipe.query.all():
        if r.tags:
            all_tags.update(tag.strip() for tag in r.tags.split(","))

    return render_template(
        "recipes.html",
        recipes=recipes,
        all_tags=sorted(all_tags),
        selected_tag=tag
    )

@main.route("/recipe/new", methods=["GET", "POST"])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            tags=form.tags.data.lower(),
            user_id=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for("main.recipes"))
    return render_template("recipe_form.html", form=form, legend="New Recipe")

@main.route("/recipe/<int:recipe_id>/edit", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user_id != current_user.id:
        flash("You are not authorized to edit this recipe.", "danger")
        return redirect(url_for("main.recipes"))
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        recipe.tags=form.tags.data.lower()
        db.session.commit()
        flash("Recipe updated successfully!", "success")
        return redirect(url_for("main.view_recipe", recipe_id=recipe.id))
    return render_template("recipe_form.html", form=form, legend="Edit Recipe")

@main.route("/recipe/<int:recipe_id>/delete", methods=["POST"])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user_id != current_user.id:
        flash("You are not authorized to delete this recipe.", "danger")
        return redirect(url_for("main.recipes"))
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted!", "success")
    return redirect(url_for("main.recipes"))

@main.route("/recipe/<int:recipe_id>/view")
@login_required
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    pst = zoneinfo.ZoneInfo("America/Los_Angeles")
    for c in recipe.comments:
        dt = c.created_at
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
        c.pst_created = dt.astimezone(pst)

    comment_form = CommentForm()
    rating_forms = {c.id: RatingForm(prefix=f"rate-{c.id}") for c in recipe.comments}

    return render_template(
        "view_recipe.html",
        recipe=recipe,
        comment_form=comment_form,
        rating_forms=rating_forms
    )

@main.route('/recipe/<int:recipe_id>/rate', methods=['POST'])
@login_required
def rate_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    value = int(request.form.get("rating", 0))

    if 1 <= value <= 5:
        from app.models import RecipeRating
        rating = RecipeRating.query.filter_by(user_id=current_user.id, recipe_id=recipe.id).first()
        if rating:
            rating.value = value
        else:
            rating = RecipeRating(user_id=current_user.id, recipe_id=recipe.id, value=value)
            db.session.add(rating)
        db.session.commit()
        flash("Rating saved!", "success")
    else:
        flash("Invalid rating value.", "danger")

    return redirect(url_for('main.view_recipe', recipe_id=recipe.id))


@main.route("/profile/<int:user_id>")
@login_required
def view_profile(user_id):
    user = User.query.get_or_404(user_id)
    posted_recipes = Recipe.query.filter_by(user_id=user.id).all()
    favorite_recipes = [fav.recipe for fav in user.favorites]
    is_self = (current_user.id == user.id)

    return render_template(
        "view_profile.html",
        user=user,
        recipes=posted_recipes,
        favorite_recipes=favorite_recipes,
        is_self=is_self
    )

@main.route('/recipe/<int:recipe_id>/comment', methods=['POST'])
@login_required
def post_comment(recipe_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            body=form.body.data,
            user_id=current_user.id,
            recipe_id=recipe_id,
            parent_id=form.parent_id.data or None
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comment posted.', 'success')
    return redirect(url_for('main.view_recipe', recipe_id=recipe_id))

@main.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        flash('Not authorized.', 'danger')
    else:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted.', 'success')
    return redirect(request.referrer)

@main.route('/comment/<int:comment_id>/rate', methods=['POST'])
@login_required
def rate_comment(comment_id):
    prefix = f"rate-{comment_id}"
    form = RatingForm(prefix=prefix)
    if form.validate_on_submit():
        rating = CommentRating.query.filter_by(
            user_id=current_user.id, comment_id=comment_id
        ).first()
        if rating:
            rating.value = form.value.data
        else:
            rating = CommentRating(
                user_id=current_user.id,
                comment_id=comment_id,
                value=form.value.data
            )
            db.session.add(rating)
        db.session.commit()
        flash('Rating saved.', 'success')
    return redirect(request.referrer)

@main.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():

        if form.email.data != current_user.email:
            existing = User.query.filter_by(email=form.email.data).first()
            if existing:
                flash("Email is already registered.", "danger")
                return redirect(url_for("main.edit_profile"))

        if form.new_password.data:
            if not form.current_password.data:
                flash("Please enter your current password to change it.", "danger")
                return redirect(url_for("main.edit_profile"))

            if not check_password_hash(current_user.password_hash, form.current_password.data):
                flash("Current password is incorrect.", "danger")
                return redirect(url_for("main.edit_profile"))

            current_user.password_hash = generate_password_hash(form.new_password.data)

        current_user.display_name = form.display_name.data
        current_user.email = form.email.data
        db.session.commit()

        flash("Profile updated successfully.", "success")
        return redirect(url_for("main.view_profile", user_id=current_user.id))

    if request.method == "GET":
        form.display_name.data = current_user.display_name
        form.email.data = current_user.email

    return render_template("edit_profile.html", form=form)

@main.route("/search")
@login_required
def search():
    query = request.args.get("q", "").strip()
    recipes = []

    if query:
        search_term = f"%{query.lower()}%"
        recipes = Recipe.query.filter(
            sa.or_(
                Recipe.title.ilike(search_term),
                Recipe.ingredients.ilike(search_term),
                Recipe.tags.ilike(search_term)
            )
        ).all()

    return render_template("search_results.html", query=query, recipes=recipes)

@main.route("/top")
@login_required
def top_recipes():
    recipes = Recipe.query.all()
    sorted_recipes = sorted(recipes, key=lambda r: r.average_rating() or 0, reverse=True)
    return render_template("top_recipes.html", recipes=sorted_recipes[:10])

@main.route('/favorite/<int:recipe_id>', methods=['POST'])
@login_required
def toggle_favorite(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    existing = Favorite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        flash("Removed from favorites.", "info")
    else:
        new_fav = Favorite(user_id=current_user.id, recipe_id=recipe_id)
        db.session.add(new_fav)
        db.session.commit()
        flash("Saved to favorites!", "success")

    return redirect(request.referrer or url_for("main.recipes"))

@main.route('/favorites')
@login_required
def view_favorites():
    favorites = current_user.favorites.all()
    recipes = [fav.recipe for fav in favorites]
    return render_template("favorites.html", recipes=recipes)
