from sqlmodel import Session
from .domain import User, Person

def create_data(engine, admin_pw_hash):
	with Session(engine) as session:
		admin = User(username="admin", password="admin", email="admin@it.com", full_name="Admin User", hashed_password=admin_pw_hash)
		session.add(admin)

		person1 = Person(full_name="John Doe", age=22, sex="M")
		person2 = Person(full_name="Jane Doe", age=21, sex="F")
		session.add(person1)
		session.add(person2)

		session.commit()
