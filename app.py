from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "s2+VjoRiAYCf4EZzbQ=="

# TODO: Fill in methods and routes

@app.route("/", methods = ["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        success = False

        for student in db_session.query(Student).all():
            if(username == student.username):
                if(password == student.password):
                    session["username"] = username
                    success = True
        
        if(success == True):
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password. Try again.", "error")
            return render_template("index.html")


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if (request.method == "GET"):
        return render_template("signup.html")
    elif (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        if username in db_session.query(Student.username).all():
            flash("That username is already taken. Try again.", "error")
            return render_template("signup.html")
        
        student = Student(username = username, password = password)
        db_session.add(student)
        db_session.commit()
        session["username"] = username

        return render_template("index.html")

@app.route("/home")
def home() :
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

def get_unenrolled():
    student = db_session.query(Student).where(Student.username == session["username"]).first()
    all_courses = db_session.query(Course).all()
    course_list = []
    for course in all_courses:
        if(course not in student.courses):
            course_list.append(course)
    return course_list

@app.route("/add", methods = ["GET", "POST"])
def add():
    if (request.method == "GET"):
        return render_template("add.html", course_list = get_unenrolled())
    elif (request.method == "POST"):
        course_id = request.form["course"]
        new_en = Enrollment(course_id = course_id, student_id = session["username"])
        db_session.add(new_en)
        db_session.commit()
    return render_template("add.html", course_list = get_unenrolled())        

@app.route("/drop", methods = ["GET", "POST"])
def drop():
    if (request.method == "GET"):
        student = db_session.query(Student).where(Student.username == session["username"]).first()
        return render_template("drop.html", course_list = student.courses)
    elif (request.method == "POST"):
        course_id = request.form["course"]
        all_en = db_session.query(Enrollment).where(Enrollment.student_id == session["username"]).all()
        for en in all_en:
            if(en.course_id == course_id):
                db_session.delete(en)
                db_session.commit()
        student = db_session.query(Student).where(Student.username == session["username"]).first()
        return render_template("drop.html", course_list = student.courses)

@app.route("/change")
def change():
    return render_template("change.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port = 5001)
