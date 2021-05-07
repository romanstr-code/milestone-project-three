# Imported Filesw
import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
# Route to Home Page
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/french_press")
def french_press():
    return render_template(
        "french_press.html",
        recipes=mongo.db.recipes.find({"category_name": "French Press"})
        .sort("recipe_name"))


@app.route("/siphon")
def siphon():
    return render_template(
        "siphon.html",
        recipes=mongo.db.recipes.find({"category_name": "Siphon Method"})
        .sort("recipe_name"))


@app.route("/turkish")
def turkish():
    return render_template(
        "turkish.html",
        recipes=mongo.db.recipes.find({"category_name": "Turkish Method"})
        .sort("recipe_name"))


@app.route("/pour_over")
def pour_over():
    return render_template(
        "pour_over.html",
        recipes=mongo.db.recipes.find({"category_name": "Pour Over Method"})
        .sort("recipe_name"))


@app.route("/aeropress")
def aeropress():
    return render_template(
        "aeropress.html",
        recipes=mongo.db.recipes.find({"category_name": "Aeropress Method"})
        .sort("recipe_name"))


@app.route("/iced_coffee")
def iced_coffee():
    return render_template(
        "iced_coffee.html",
        recipes=mongo.db.recipes.find({"category_name": "Iced Method"})
        .sort("recipe_name"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome,{}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect("login")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Send User Input to DB
    if request.method == "POST":
        recipes = {
            "url": request.form.get("url"),
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingridients": request.form.get("ingridients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        # Post the User Input to MDB
        mongo.db.recipes.insert_one(recipes)
        flash("Thank You for your Recipe!")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipes/<recipes_id>", methods=["GET", "POST"])
def edit_recipe(recipes_id):
    if request.method == "POST":
        submit = {
            "url": request.form.get("url"),
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingridients": request.form.get("ingridients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }

        mongo.db.recipes.update({"_id": ObjectId(recipes_id)}, submit)
        flash("Yeeey! Edited with Success!")
        return redirect(url_for('recipes'))

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template("edit_recipe.html", recipes=recipes)


@app.route("/delete_recipe/<recipes_id>")
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
    flash("Deleted Permanently!")
    return redirect(url_for('recipes'))


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/about")
def about():
    return render_template("about_us.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)