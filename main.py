

from fastapi import FastAPI, Request, HTTPException, Depends , Form
from sqlalchemy import create_engine, Select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from fastapi.templating import Jinja2Templates

DB_URL = 'postgresql+psycopg://sd4:sd4@localhost:5432/insta'
engine = create_engine(DB_URL, echo=True)

# 모델정의 > MVC의 모델 

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    # title: Mapped[str]
    content: Mapped[str]


app = FastAPI()
templates = Jinja2Templates(directory='templates')

def get_db():
    with Session(engine) as db:
        yield db 



@app.get('/')
def home():
    return {'hi': 'hello'}

@app.get('/posts')
def post_list(request: Request , db: Session = Depends(get_db)):
    # with Session(engine) as db :
    posts = db.scalars(Select(Post)).all()

    return templates.TemplateResponse(

            request=request,
            name='list.html',
            context={'posts': posts}

    )

