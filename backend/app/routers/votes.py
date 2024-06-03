from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import oauth2_scheme, get_session
from sqlmodel import Session, select
from ..domain import Votes
from ..commands import VoteCommand
from ..dependencies import get_current_user

router = APIRouter(
	prefix="/votes",
	tags=["votes"],
	dependencies=[Depends(oauth2_scheme)],
)

@router.get("/")
def get_votes(session: Session = Depends(get_session)):
	votes = session.exec(select(Votes)).all()
	return votes

@router.post("/")
def create_vote(vote: VoteCommand, session: Session = Depends(get_session), user = Depends(get_current_user)):
	new_vote = Votes(
		user_id=user.id,
		person_id=vote.person_id,
		position_id=vote.position_id
	)

	session.add(new_vote)
	session.commit()
	return vote
