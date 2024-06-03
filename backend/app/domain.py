from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint

class Position(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	name: str = Field(max_length=100, unique=True)
	description: str = Field(max_length=100)

	persons: list["Person"] = Relationship(back_populates="position")
	votes: list["Votes"] = Relationship(back_populates="position")

class User(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	username: str = Field(max_length=100, unique=True)
	email: str = Field(max_length=100)
	full_name: str = Field(max_length=100)
	disabled: bool = Field(default=False)
	hashed_password: str

	votes: list["Votes"] = Relationship(back_populates="user")

class Person(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	full_name: str = Field(max_length=100)
	age: int
	sex: str = Field(max_length=1)

	position_id: int | None = Field(default=None, foreign_key="position.id")
	position: Position | None = Relationship(back_populates="persons")

	votes: list["Votes"] = Relationship(back_populates="person")

class Votes(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	
	user_id: int = Field(foreign_key="user.id")
	user: User = Relationship(back_populates="votes")

	person_id: int = Field(foreign_key="person.id")
	person: Person = Relationship(back_populates="votes")

	position_id: int = Field(foreign_key="position.id")
	position: Position = Relationship(back_populates="votes")

	# person, position and user have to be unique together
	__table_args__ = (UniqueConstraint("user_id", "person_id", "position_id"),)
