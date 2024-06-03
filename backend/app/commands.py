from pydantic import BaseModel

class LoginCommand(BaseModel):
	username: str
	password: str
     
class RegisterCommand(BaseModel):
	username: str
	password: str
	email: str
	full_name: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None

class UserCommand(BaseModel):
	username: str
	email: str
	full_name: str
	disabled: bool

class VoteCommand(BaseModel):
	person_id: int
