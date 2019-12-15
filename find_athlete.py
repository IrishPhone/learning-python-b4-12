import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from datetime import timedelta

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

class Athlete(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key = True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key = True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)


def main():
    entered_id = int(input("User ID: "))
    users = session.query(User).all()
    athletes = session.query(Athlete).all()

    user_ids = [u.id for u in users]
    same_height = Athlete()

    if entered_id in user_ids:
        entered_user = [u for u in users if u.id == entered_id][0]
        same_height = Athlete()
        min_diff = 1000
        for a in athletes:
            if type(a.height) == type(1.0):
                tmp = abs(float(a.height) - entered_user.height)
                if min_diff > tmp:
                    min_diff = tmp
                    same_height.id = a.id
                    same_height.name = a.name
                    same_height.height = a.height
                else:
                    continue
            else:
                continue

        print("The user's height is", entered_user.height, "m")
        print("The user's birthdate is", entered_user.birthdate)
        print("The nearest height athlete is", same_height.id, same_height.name, same_height.height, "m")

        same_birthdate = Athlete()
        user_bd = datetime.strptime(entered_user.birthdate, "%Y-%m-%d")
        ath_bd = datetime.strptime(athletes[0].birthdate, "%Y-%m-%d") 
        diff_bd = 100000000.0
        
        for a in athletes:
            ath_bd = datetime.strptime(a.birthdate, "%Y-%m-%d")
            if diff_bd > abs( (user_bd - ath_bd).total_seconds() ):
                diff_bd = abs( (user_bd - ath_bd).total_seconds() )
                same_birthdate.id = a.id
                same_birthdate.name = a.name
                same_birthdate.birthdate = a.birthdate
                same_birthdate.sport = a.sport


        print("The nearest birthdate athlete is: ", same_birthdate.sport, same_birthdate.id, same_birthdate.name, same_birthdate.birthdate)
        
    else:
        print("The user is not found, try another ID")

    #session.add(user)
    #session.commit()

if __name__ == "__main__":
    main()
