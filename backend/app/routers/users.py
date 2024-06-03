from fastapi import APIRouter, Depends
from typing import Annotated
from .. import domain
from ..dependencies import get_current_active_user
from ..commands import UserCommand

router = APIRouter(
	prefix="/users",
	tags=["users"],
)

@router.get("/me")
async def read_users_me(
    current_user: Annotated[domain.User, Depends(get_current_active_user)],
) -> UserCommand:
    user = UserCommand(
		username=current_user.username,
		email=current_user.email,
		full_name=current_user.full_name,
	)
    return user
