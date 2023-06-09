from models import *
from sqlalchemy import func
from database import init_db, db_session

# Initialize our database
init_db()

# Add new courses
course1 = Course(name = "AP Lit", block = "A", image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")
course2 = Course(name = "AP Physics 2", block = "B", image = "https://media.istockphoto.com/id/855195698/vector/chemical-test-tube-pictogram-icon-laboratory-glassware-or-beaker-equipment-isolated-on-white.jpg?s=612x612&w=0&k=20&c=-GCYlp7-Nbrarm4I9E4HRi22anLS4UTfTO7RBDW152c=")
course3 = Course(name = "AP Calculus BC", block = "C", image = "https://media.istockphoto.com/id/1392292723/vector/vector-doodle-illustration-school-calculator-isolated-on-white.jpg?s=612x612&w=0&k=20&c=2dqceaXd0QxfWLY22JSETfdq3GfIntJPSMW14FVmLdg=")
course4 = Course(name = "AP Euro", block = "D", image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")
course5 = Course(name = "Choir", block = "A", image = "https://t3.ftcdn.net/jpg/02/83/45/20/360_F_283452054_gT96gUaL4FN2o6UT1drEAhOSkx1IQXNw.jpg")
course6 = Course(name = "AP Comp Sci", block = "B", image = "https://media.istockphoto.com/id/855195698/vector/chemical-test-tube-pictogram-icon-laboratory-glassware-or-beaker-equipment-isolated-on-white.jpg?s=612x612&w=0&k=20&c=-GCYlp7-Nbrarm4I9E4HRi22anLS4UTfTO7RBDW152c=")
course7 = Course(name = "Pre-Calculus", block = "C", image = "https://media.istockphoto.com/id/1392292723/vector/vector-doodle-illustration-school-calculator-isolated-on-white.jpg?s=612x612&w=0&k=20&c=2dqceaXd0QxfWLY22JSETfdq3GfIntJPSMW14FVmLdg=")
course8 = Course(name = "Ethnic Studies", block = "D", image = "https://media.istockphoto.com/vectors/history-class-set-of-objects-vector-id589421312?k=20&m=589421312&s=612x612&w=0&h=jadxqJSeDUvf9zDfd_z4gAQ6-7Sj8VVciWRiTTW--YU=")

db_session.add_all([course1, course2, course3, course4, course5, course6, course7, course8])
db_session.commit()

