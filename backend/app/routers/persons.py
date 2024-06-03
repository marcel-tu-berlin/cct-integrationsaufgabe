from fastapi import APIRouter, Depends
from ..dependencies import oauth2_scheme, get_session
from sqlmodel import Session, select
from ..domain import Person

router = APIRouter(
	prefix="/persons",
	tags=["persons"],
	dependencies=[Depends(oauth2_scheme)],
)

@router.get("/")
def get_persons(session: Session = Depends(get_session)):
	persons = session.exec(select(Person)).all()
	return persons

@router.post("/")
def create_person(person: Person, session: Session = Depends(get_session)):
	session.add(person)
	session.commit()
	return person