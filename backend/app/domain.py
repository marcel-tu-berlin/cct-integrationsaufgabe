from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	username: str = Field(max_length=100, unique=True)
	email: str = Field(max_length=100)
	full_name: str = Field(max_length=100)
	disabled: bool = Field(default=False)
	hashed_password: str

class Person(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	full_name: str = Field(max_length=100)
	age: int
	sex: str = Field(max_length=1)

