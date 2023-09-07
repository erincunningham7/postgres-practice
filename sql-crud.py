from sqlalchemy import (
    create_engine, Column, Integer, String
)

# the python classes we create are subclasses of the declarative_base
from sqlalchemy.ext.declarative import declarative_base
# in order to ask for a session with sessionmaker
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
# The 'base' class will grab the metadata produced by our db table schema
# and creates a subclass to map everything back here within the 'base' variable
base = declarative_base()

# create a class based model for the programmer table


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# make a new instance of the sessionmaker and point to our db engine to use our db
Session = sessionmaker(db)
# open an actual session
session = Session()

# create the db using declarative_base subclass
base.metadata.create_all(db)

# creating records on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)

# commit our session to the db
session.commit()

# query the db to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
