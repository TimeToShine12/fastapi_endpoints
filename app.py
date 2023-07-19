import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db
from models import User, Post, Feed
from schemas import UserGet, PostGet, FeedGet
from typing import List

app = FastAPI()


# Получаем user по id
@app.get("/user/{id}", response_model=UserGet, summary="Get user by id")
def get_user(id: int, db: Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).one_or_none()
    if not result:
        raise HTTPException(404, f'User with id = {id} not found')
    else:
        return result


# Получаем post по id
@app.get("/post/{id}", response_model=PostGet, summary="Get post by id")
def get_post(id: int, db: Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if not result:
        raise HTTPException(404, f'Post with id = {id} not found')
    else:
        return result


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed) \
        .join(User) \
        .filter(User.id == id) \
        .order_by(Feed.time.desc()) \
        .limit(limit) \
        .all()


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed)\
        .join(Post)\
        .filter(Post.id == id)\
        .order_by(Feed.time.desc())\
        .limit(limit)\
        .all()


@app.get("/post/recommendations/", response_model=List[PostGet])
def get_liked_post(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Post)\
        .select_from(Feed)\
        .filter(Feed.action == "like")\
        .join(Post)\
        .group_by(Post.id)\
        .order_by(func.count(Post.id).desc())\
        .limit(limit)\
        .all()


# Для доступа к переменным окружения
# вызываем метод load_dotenv из библиотеки dotenv
if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app)
