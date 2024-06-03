from sqlmodel import Session
from .domain import User, Person, Votes, Position

def create_data(engine, admin_pw_hash):
	with Session(engine) as session:
		admin = User(username="admin", password="admin", email="admin@it.com", full_name="Admin User", hashed_password=admin_pw_hash)
		session.add(admin)

		person1 = Person(full_name="John Doe", age=22, sex="M")
		person2 = Person(full_name="Jane Doe", age=21, sex="F")
		session.add(person1)
		session.add(person2)

		position1 = Position(name="CEO", description="Chief Executive Officer")
		position2 = Position(name="CTO", description="Chief Technology Officer")
		session.add(position1)
		session.add(position2)

		vote1 = Votes(user=admin, person=person1, position=position1)
		vote2 = Votes(user=admin, person=person2, position=position2)
		session.add(vote1)
		session.add(vote2)

		session.commit()
