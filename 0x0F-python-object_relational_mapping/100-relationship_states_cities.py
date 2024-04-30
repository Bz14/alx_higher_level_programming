#!/usr/bin/python3
""" List city from database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    url = f"mysql://{user_name}:{password}"
    url += f"@localhost:3306/{dbName}"
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California")
    session.add(california)
    san_francisco = City(name="San Francisco")
    san_francisco.state = california
    session.add(san_francisco)
    session.commit()
