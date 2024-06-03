from sqlmodel import Session
from .domain import User, Person, Votes, Position

def create_data(engine, admin_pw_hash):
	with Session(engine) as session:
		admin = User(username="admin", email="admin@it.com", full_name="Admin User", hashed_password=admin_pw_hash)
		test = User(username="test", email="test@company.com", full_name="Test User", hashed_password=admin_pw_hash)
		dummy = User(username="dummy", email="dummy@company.com", full_name="Dummy User", hashed_password=admin_pw_hash)
		session.add(dummy)
		session.add(test)
		session.add(admin)

		position1 = Position(name="CEO", description="Chief Executive Officer")
		position2 = Position(name="CTO", description="Chief Technology Officer")
		session.add(position1)
		session.add(position2)

		person1 = Person(full_name="John Doe", age=22, sex="M", position=position1)
		person2 = Person(full_name="Jane Doe", age=21, sex="F", position=position2)
		person3 = Person(full_name="Jack Doe", age=45, sex="M", position=position1)
		person4 = Person(full_name="Jill Doe", age=33, sex="F", position=position2)
		session.add(person1)
		session.add(person2)
		session.add(person3)
		session.add(person4)

		vote1 = Votes(user=admin, person=person1, position=position1)
		vote2 = Votes(user=admin, person=person2, position=position2)
		vote3 = Votes(user=test, person=person1, position=position1)
		vote4 = Votes(user=dummy, person=person2, position=position1)
		session.add(vote1)
		session.add(vote2)
		session.add(vote3)
		session.add(vote4)

		session.commit()
