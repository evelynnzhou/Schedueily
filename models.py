"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    username = Column("username", TEXT, primary_key = True)
    password = Column("password", TEXT, nullable = False)

    courses = relationship("Course", secondary = "enrollments", back_populates = "students")

    def __repr__(self):
        return "@" + self.username

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column("id", INTEGER, primary_key = True)
    course_id = Column("course_id", TEXT, ForeignKey('courses.id'))
    student_id = Column("student_id", TEXT, ForeignKey('students.username'))


class Course(Base):
    __tablename__ = "courses"

    id = Column("id", INTEGER, primary_key = True)
    name = Column("name", TEXT, nullable = False)
    block = Column("block", TEXT, nullable = False)
    # teacher_id = Column("teacher_id", ForeignKey('teachers.id'))
    image = Column("image", TEXT, nullable = False)

    students = relationship("Student", secondary = "enrollments", back_populates = "courses")
    # teacher = relationship("Teacher", back_populates = "courses")

    def __repr__(self):
        return self.name

# class Teacher(Base):
#     __tablename__ = "teachers"

#     id = Column("id", INTEGER, primary_key = True)
#     first_name = Column("first_name", TEXT, nullable = False)
#     last_name = Column("last_name", TEXT, nullable = False)

#     courses = relationship("Course", back_populates = "teacher")

# TODO: Complete your models
    