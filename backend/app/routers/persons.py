from fastapi import APIRouter, Depends, HTTPException, status
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
	session.exec(select(Person).where(Person.full_name == person.full_name)).first()
	if person:
		raise HTTPException(status_code=400, detail="Person already exists")

	session.add(person)
	session.commit()
	return person

@router.delete("/{person_id}")
def delete_person(person_id: int, session: Session = Depends(get_session)):
	person = session.get(Person, person_id)
	session.delete(person)
	session.commit()
	return person
