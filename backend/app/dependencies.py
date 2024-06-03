from fastapi import Depends, HTTPException, status
from typing import Annotated
from .domain import User
from .commands import TokenData
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from sqlmodel import Session, select, create_engine, SQLModel
from datetime import datetime, timedelta, timezone
import os

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

def remove_db():
	if os.path.exists(sqlite_file_name):
		os.remove(sqlite_file_name)

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

SECRET_KEY = "f0bae87552350aeeec376cbfffbd3d257d63d5e8a6a345e4b02275fab4bd2a63"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str) -> User:
	with Session(engine) as session:
		user = session.exec(select(User).where(User.username == username)).first()
		return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
	with Session(engine) as session:
		user = session.exec(select(User).where(User.username == username)).first()
		if not user:
			return False
		if not verify_password(password, user.hashed_password):
			return False
		return user

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_session():
    with Session(engine) as session:
        yield session