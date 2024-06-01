from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/login")
def login(username: str, password: str):
    return {"username": username, "password": password}
