import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

class AnotherUser(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key = True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)


def create_record():
    user_firstname = input("First name: ")
    user_lastname = input("Second name: ")
    user_gender = input("Gender: ")
    user_email = input("Email: ")
    user_birthdate = input("Birth date (YYYY-MM-DD): ")
    user_height = float( input("Height in meters: ") )

    user = AnotherUser(
        first_name=user_firstname,
        last_name=user_lastname,
        gender=user_gender,
        email=user_email,
        birthdate=user_birthdate,
        height=user_height
        )
    session.add(user)
    session.commit()

    print("The record is added to the base successfully")

def main():

    choice = "1"
    while choice == "1":
        choice = input("1 - Add a user\n2 - exit\n")
        if choice == "1":
            create_record()
        else:
            break


    



if __name__ == "__main__":
    main()
