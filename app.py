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

        user = Student.query.filter_by(username = username).first()
        pw = Student.query.filter_by(password = password).first()
        
        #checks if username exists and password matches
        if (user is None) or (pw is None):
            flash("Incorrect username or password. Try again.", "error")
            return render_template("index.html")
        else:
            session["username"] = username
            return redirect(url_for("home"))


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if (request.method == "GET"):
        return render_template("signup.html")
    elif (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        user = Student.query.filter_by(username = username).first()

        if (user is not None):
            flash("That username is already taken. Try again.", "error")
            return render_template("signup.html")
        
        # creates new student and adds it to database
        student = Student(username = username, password = password)
        db_session.add(student)
        db_session.commit()
        session["username"] = username

        return redirect(url_for("login"))

@app.route("/home")
def home() :
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

# creates a list of courses that the student is not yet enrolled in
def get_unenrolled():
    student = db_session.query(Student).where(Student.username == session["username"]).first()
    all_courses = db_session.query(Course).all()
    course_list = []
    for course in all_courses:
        if(course not in student.courses):
            course_list.append(course)
    return course_list

# checks if a block is free to add a class
def check_free(course_id):
    student = db_session.query(Student).where(Student.username == session["username"]).first()
    for course in student.courses:
        if(course.block == db_session.query(Course).where(Course.id == course_id).first().block):
            return False
    return True

@app.route("/add", methods = ["GET", "POST"])
def add():
    if (request.method == "GET"):
        return render_template("add.html", course_list = get_unenrolled())
    elif (request.method == "POST"):
        course_id = request.form["course"]
        if(check_free(course_id) == False):
            flash("You already have a class during this block.", "error")
        else:
            # creates new enrollment if block isn't already filled
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
        # deletes the enrollment whose course id matches w/ the obtained course id 
        for en in all_en:
            if(en.course_id == course_id):
                db_session.delete(en)
                db_session.commit()
        student = db_session.query(Student).where(Student.username == session["username"]).first()
        return render_template("drop.html", course_list = student.courses)

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port = 5001)
