from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "s2+VjoRiAYCf4EZzbQ=="

# TODO: Fill in methods and routes

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        session["username"] = username
        return redirect(url_for("home"))

@app.route("/home")
def home() :
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

@app.route("/add")
def add():
    if request.method == "GET":
        course_list = db_session.query(Course).all()
        return render_template("add.html", course_list = course_list)

@app.route("/drop")
def drop():
    return render_template("drop.html")

@app.route("/change")
def change():
    return render_template("change.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port = 5001)
