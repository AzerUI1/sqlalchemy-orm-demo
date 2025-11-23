from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Base ORM class
Base = declarative_base()


# User model representing 'users' table
class User(Base):
__tablename__ = 'users'
id = Column(Integer, primary_key=True)
name = Column(String)
age = Column(Integer)


# Create SQLite database
engine = create_engine("sqlite:///mydb.db")


# Create all tables
Base.metadata.create_all(engine)


# Create DB session
Session = sessionmaker(bind=engine)
session = Session()


# Insert users
session.query(User).delete() # clean table for nice results
session.commit()


u1 = User(name="Azer", age=14)
u2 = User(name="Leyla", age=16)
session.add_all([u1, u2])
session.commit()


print("Inserted 2 Users")


# Select all
all_users = session.query(User).all()
print("All users:")
for u in all_users:
print(u.id, u.name, u.age)


# Filter
young = session.query(User).filter(User.age < 18).all()
print("Users younger than 18:")
for u in young:
print(u.name)


# Update
azer = session.query(User).filter_by(name="Azer").first()
if azer:
azer.age = 15
session.commit()
print("Updated Azer's age to 15")


# Delete
leyla = session.query(User).filter_by(name="Leyla").first()
if leyla:
session.delete(leyla)
session.commit()
print("Deleted Leyla")


# Final output
print("Final table content:")
for u in session.query(User).all():
print(u.id, u.name, u.age)


session.close()
