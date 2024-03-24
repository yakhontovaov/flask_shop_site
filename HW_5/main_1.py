from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
templates = Jinja2Templates(directory="./HW_5/templates")

DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


Base.metadata.create_all(bind=engine)


@app.post("/users/")
async def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.put("/users/{user_id}/")
async def update_user(user_id: int, user_data: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user_data.name
    db_user.email = user_data.email
    db_user.password = user_data.password
    db.commit()
    db.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
