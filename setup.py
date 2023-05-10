from models import *
from sqlalchemy import func
from database import init_db, db_session

# Initialize our database
init_db()

# Add new courses
course1 = Course(name = "AP Lit", block = "A", teacher_id = 1, image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")
course2 = Course(name = "AP Physics 2", block = "B", teacher_id = 2, image = "https://media.istockphoto.com/id/855195698/vector/chemical-test-tube-pictogram-icon-laboratory-glassware-or-beaker-equipment-isolated-on-white.jpg?s=612x612&w=0&k=20&c=-GCYlp7-Nbrarm4I9E4HRi22anLS4UTfTO7RBDW152c=")
course3 = Course(name = "AP Calculus BC", block = "C", teacher_id = 3, image = "https://media.istockphoto.com/id/1392292723/vector/vector-doodle-illustration-school-calculator-isolated-on-white.jpg?s=612x612&w=0&k=20&c=2dqceaXd0QxfWLY22JSETfdq3GfIntJPSMW14FVmLdg=")
course4 = Course(name = "AP Euro", block = "D", teacher_id = 4, image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")
course5 = Course(name = "Choir", block = "A", teacher_id = 5, image = "https://t3.ftcdn.net/jpg/02/83/45/20/360_F_283452054_gT96gUaL4FN2o6UT1drEAhOSkx1IQXNw.jpg")
course6 = Course(name = "AP Comp Sci", block = "B", teacher_id =6, image = "https://media.istockphoto.com/id/855195698/vector/chemical-test-tube-pictogram-icon-laboratory-glassware-or-beaker-equipment-isolated-on-white.jpg?s=612x612&w=0&k=20&c=-GCYlp7-Nbrarm4I9E4HRi22anLS4UTfTO7RBDW152c=")
course7 = Course(name = "Pre-Calculus", block = "C", teacher_id = 3, image = "https://media.istockphoto.com/id/1392292723/vector/vector-doodle-illustration-school-calculator-isolated-on-white.jpg?s=612x612&w=0&k=20&c=2dqceaXd0QxfWLY22JSETfdq3GfIntJPSMW14FVmLdg=")
course8 = Course(name = "Ethnic Studies", block = "D", teacher_id = 4, image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")

db_session.add_all([course1, course2, course3, course4, course5, course6, course7, course8])
db_session.commit()


# Add new enrollments
en1 = Enrollment(course_id = 1, student_id = "a")
en2 = Enrollment(course_id = 2, student_id = "a")
en3 = Enrollment(course_id = 3, student_id = "a")
en4 = Enrollment(course_id = 4, student_id = "a")
en5 = Enrollment(course_id = 5, student_id = "b")
en6 = Enrollment(course_id = 6, student_id = "b")
en7 = Enrollment(course_id = 7, student_id = "b")
en8 = Enrollment(course_id = 8, student_id = "b")

db_session.add_all([en1, en2, en3, en4, en5, en6, en7, en8])
db_session.commit()

