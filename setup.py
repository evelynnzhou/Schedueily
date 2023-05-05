from models import *
from sqlalchemy import func
from database import init_db, db_session

# Initialize our database
init_db()

# Add new students
student1 = Student(username = "a", password = "123")
student2 = Student(username = "b", password = "123")

db_session.add_all([student1, student2])
db_session.commit()

# Add new courses
course1 = Course(name = "AP Lit", block = "A", teacher_id = 1)
course2 = Course(name = "AP Physics 2", block = "B", teacher_id = 2)
course3 = Course(name = "AP Calculus BC", block = "C", teacher_id = 3)
course4 = Course(name = "AP Euro", block = "D", teacher_id = 4)
course5 = Course(name = "Choir", block = "A", teacher_id = 5)
course6 = Course(name = "AP Comp Sci", block = "B", teacher_id =6)
course7 = Course(name = "Pre-Calculus", block = "C", teacher_id = 3)
course8 = Course(name = "Ethnic Studies", block = "D", teacher_id = 4)

db_session.add_all([course1, course2, course3, course4, course5, course6, course7, course8])
db_session.commit()

# Add new teachers
teacher1 = Course(first_name = "Anne", last_name = "Harris")
teacher2 = Course(first_name = "James", last_name = "Dann")
teacher3 = Course(first_name = "Reeve", last_name = "Garrett")
teacher4 = Course(first_name = "Katharine", last_name = "Hanson")
teacher5 = Course(first_name = "Philip", last_name = "Harris")
teacher6 = Course(first_name = "Nandhini", last_name = "Namasivayam")

# Add new enrollments
en1 = Enrollment(course_id = 1, student_id = 1)
en2 = Enrollment(course_id = 2, student_id = 1)
en3 = Enrollment(course_id = 3, student_id = 1)
en4 = Enrollment(course_id = 4, student_id = 1)
en5 = Enrollment(course_id = 5, student_id = 2)
en6 = Enrollment(course_id = 6, student_id = 2)
en7 = Enrollment(course_id = 7, student_id = 2)
en8 = Enrollment(course_id = 8, student_id = 2)

