from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import oauth2_scheme, get_session
from sqlmodel import Session, select
from ..domain import Position, PositionPublicWithVotesAndPersons

router = APIRouter(
	prefix="/positions",
	tags=["positions"],
	dependencies=[Depends(oauth2_scheme)],
)

@router.get("/", response_model=list[PositionPublicWithVotesAndPersons])
def get_positions(session: Session = Depends(get_session)):
	positions = session.exec(select(Position)).all()
	return positions

# Get a single position by ID with persons and votes
@router.get("/{position_id}", response_model=PositionPublicWithVotesAndPersons)
def get_position(position_id: int, session: Session = Depends(get_session)):
	position = session.get(Position, position_id)
	if position is None:
		raise HTTPException(status_code=404, detail="Position not found")
	return position
