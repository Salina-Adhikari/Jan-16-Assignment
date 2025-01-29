# Language=Query
# SQL and no SQL
# mobile application=SQL lite3
# cursor runs sql
# in we want to build connection in another the primary becomes foreign key
# commmit makes change shown
# *all 

# Using SQLite3 to interact with a database
import sqlite3
connection=sqlite3.connect("store.db")
cursor=connection.cursor()
# Create a table of products
cursor.execute('''CREATE TABLE IF NOT EXISTS products(
               id INTEGER Primary Key,
               name TEXT NOT NULL,
               price REAL NOT NULL)'''
               )
# Insrt data
cursor.execute("INSERT INTO products(name,price)VALUES(?,?)",("Laptop",999.999))
connection.commit()

# # Insert data 
# cursor.execute("SELECT * FROM products")
# for row in cursor.fetchall():
#     print(row)

# connection.close()
# # Fetch data
# cursor.execute


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price=Column(Float,nullable=False)

#Create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a new product
new_product=Product(name="Tablet",price=299.99)
session.add(new_product)
session.commit()

# Query products
for product in session.query(Product):
    print(product.name,product.price)





import sqlite3
connection = sqlite3.connect("Book.db")
cursor = connection.cursor()

# Corrected CREATE TABLE statement
cursor.execute('''
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Insert data
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life or Death", "Salina Adhikari", 600.23))
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life on Verge", "APM on Line", 700.23))
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Hello from Other side", "lilly", 400))
connection.commit()

# Fetch and print data
cursor.execute("SELECT * FROM book")
for row in cursor.fetchall():
    print(row)

# Close the connection
connection.close()

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email=Column(String,nullable=False)

engine = create_engine('sqlite:///record.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


john_doe = User(name="John Doe", email="old.email@example.com")
session.add(john_doe)
session.commit()


user = session.query(User).filter(User.name == "John Doe").first()
if user:
    user.email="new.email@example.com"
    session.commit()
    print("Email updated successfully.")

else:
    print("User not found")



if user:
    user.email = "new.email@example.com"
    session.commit()
    print("Email updated successfully.")
else:
    print("User not found.")

updated_user = session.query(User).filter(User.name == "John Doe").first()
print(f"Updated User Record: Name: {updated_user.name}, Email: {updated_user.email}")
