from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

accountsDB = []

# post model
class Account(BaseModel):
    id: int
    email: Text
    password: Text

@app.get("/")
def root():
    return{"message":"Hello World!"}

@app.get("/accounts")
def get_accounts():
    return accountsDB

@app.post("/accounts")
def post_accounts(account: Account):
    accountsDB.append(account.dict())
    return accountsDB[-1]