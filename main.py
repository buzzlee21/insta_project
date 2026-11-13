

from fastapi import FastAPI, Request, HTTPException, Depends , Form
from sqlalchemy import create_engine, Select, func , ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from datetime import datetime
from pwdlib import PasswordHash
import secrets
from typing  import Annotated
from routers import posts, auth, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(users.router)

app.mount('/media', StaticFiles(directory='media'), name='media')
app.mount('/static', StaticFiles(directory='static'), name='satic')

@app.get('/')
def home():
  return {'hi': 'hello'}



