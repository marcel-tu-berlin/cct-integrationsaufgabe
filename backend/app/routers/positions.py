from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import oauth2_scheme, get_session
from sqlmodel import Session, select
from ..domain import Position

router = APIRouter(
	prefix="/positions",
	tags=["positions"],
	dependencies=[Depends(oauth2_scheme)],
)

@router.get("/")
def get_positions(session: Session = Depends(get_session)):
	positions = session.exec(select(Position)).all()
	return positions

