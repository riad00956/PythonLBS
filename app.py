
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

members = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/members")
def show_members():
    return render_template("members.html", members=members)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        photo = request.form["photo"]
        bio = request.form["bio"]
        age = request.form["age"]
        members.append({
            "name": name,
            "photo": photo,
            "bio": bio,
            "age": age
        })
        return redirect("/members")
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
