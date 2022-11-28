
from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "mysecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run()