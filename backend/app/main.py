from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .data import create_data
from .dependencies import create_db_and_tables, engine, get_password_hash, remove_db
from .routers import persons, users, auth, votes

app = FastAPI(
	root_path="/api",
)

origins = [
	"http://localhost:5173",
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(persons.router)
app.include_router(votes.router)
    
@app.on_event("startup")
def on_startup():
    remove_db()
    create_db_and_tables()
    create_data(engine, get_password_hash("admin"))
