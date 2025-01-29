# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class ToDoList(Base):
#     __tablename__ = 'todolist'
#     id = Column(Integer, primary_key=True)
#     description = Column(String, nullable=False)
#     due_date=Column(String,nullable=False)


# engine = create_engine('sqlite:///mytask.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# new_todolist_1=ToDoList(description="Make  bed",due_date=2)
# new_todolist_2=ToDoList(description="Wash Clothes",due_date=3)
# new_todolist_3=ToDoList(description="Do dishes",due_date=3)


# session.add(new_todolist_1)
# session.add(new_todolist_2)
# session.add(new_todolist_3)
# session.commit()
# session.delete(new_todolist_3)
# session.commit()



# for todolist in session.query(ToDoList):
#     print(todolist.description,todolist.due_date)




#  Task: Make a book library manager that stores books in SQLite.
# Use SQLAlchemy to add, remove, and search for books.
# Query books by genre, author, or rating.

# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
# class Store(Base):
#     __tablename__ = "book"
#     id = Column(Integer, primary_key=True)
#     genre=Column(String,nullable=False)
#     author=Column(String,nullable=False)
#     rating=Column(Integer,nullable=False)

# engine = create_engine('sqlite:///favourites.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# new_book1=Store(genre="Horror",author="Ray Mon",rating=3.5)
# new_book2=Store(genre="RomCom",author="Helena",rating=5)
# new_book3=Store(genre="Anime",author="My",rating=2.1)
# new_book4=Store(genre="Self-development",author="Richard ho",rating=4.1)
# session.add_all([new_book1,new_book2,new_book3,new_book4])
# session.commit()
# session.delete(new_book3)
# session.commit()

# def search_book(search_author):
#     books= session.query(Store).filter(Store.author==search_author).first()
#     if books:
#         print(f"Book is Found{books.genre} ,{books.author} and rating{books.rating}")

    
#     else:
#         print("Book is not found")
# search_author="Helena"
# search_book(search_author)
# Task: Develop a student course enrollment system.
# Store students and their enrolled courses in a database.
# Allow adding and updating course enrollments.
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class College(Base):
    __tablename__="college"
    id=Column(Integer,primary_key=True)
    student_name=Column(String,nullable=False)
    student_course=Column(String,nullable=False)

engine = create_engine('sqlite:///CollegeData.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_name1=College(student_name="Rosie Posie",student_course="BIT")
new_name2=College(student_name="Salina Adhikari",student_course="Nursing")
session.add_all([new_name1,new_name2])
session.commit()

def add_student(search_student,search_course):
   students=session.query(College).filter(College.student_name==search_student,College.student_course==search_course).first()
   if students:
       print("Student has already been enrolled")
   else:
       new_student=College(student_name=search_student,student_course=search_course)
       session.add(new_student)
       session.commit()
       print(f"Student has data has been added{search_student} and {search_course}")
search_student="Lilly"
search_course="Management"
add_student(search_student,search_course)
       



