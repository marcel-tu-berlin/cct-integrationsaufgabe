from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..commands import RegisterCommand, Token
from ..domain import User
from ..dependencies import get_password_hash, get_session, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from sqlmodel import Session
from fastapi import HTTPException, status
from datetime import timedelta
from typing import Annotated

router = APIRouter(
	prefix="/auth",
	tags=["auth"],
)

@router.post("/token")
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.post("/register")
def register(user: RegisterCommand, session: Session = Depends(get_session)):
		password = user.password        
		
		user = User(
			username=user.username,
			email=user.email,
			full_name=user.full_name,
			hashed_password=get_password_hash(user.password),
		)
		session.add(user)
		session.commit()
		session.refresh(user)
                
		user = authenticate_user(user.username, password)
		access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
		access_token = create_access_token(
			data={"sub": user.username}, expires_delta=access_token_expires
		)
		return Token(access_token=access_token, token_type="bearer")
        