from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint

class PositionBase(SQLModel):
	name: str = Field(max_length=100, unique=True)
	description: str = Field(max_length=100)

class Position(PositionBase, table=True):
	id: int | None = Field(default=None, primary_key=True)

	persons: list["Person"] = Relationship(back_populates="position")
	votes: list["Votes"] = Relationship(back_populates="position")

class PositionPublic(PositionBase):
	id: int

class PositionPublicWithVotesAndPersons(PositionPublic):
	persons: list["Person"] = []
	votes: list["Votes"] = []

class User(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	username: str = Field(max_length=100, unique=True)
	email: str = Field(max_length=100)
	full_name: str = Field(max_length=100)
	disabled: bool = Field(default=False)
	hashed_password: str

	votes: list["Votes"] = Relationship(back_populates="user")

class PersonBase(SQLModel):
	full_name: str = Field(max_length=100)
	age: int
	sex: str = Field(max_length=1)

class Person(PersonBase, table=True):
	id: int | None = Field(default=None, primary_key=True)

	position_id: int | None = Field(default=None, foreign_key="position.id")
	position: Position | None = Relationship(back_populates="persons")

	votes: list["Votes"] = Relationship(back_populates="person")

class PersonPublic(PersonBase):
	id: int

class PersonPublicWithVotes(PersonPublic):
	votes: list["Votes"] = []
	position: PositionPublic | None


class Votes(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	
	user_id: int = Field(foreign_key="user.id")
	user: User = Relationship(back_populates="votes")

	person_id: int = Field(foreign_key="person.id")
	person: Person = Relationship(back_populates="votes")

	position_id: int = Field(foreign_key="position.id")
	position: Position = Relationship(back_populates="votes")

	# position and user have to be unique together, since a user can only vote once for a position
	__table_args__ = (UniqueConstraint("user_id", "position_id"),)
