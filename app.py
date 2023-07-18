from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
import psycopg2
import uvicorn
import os

from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection

app = FastAPI()


def get_db():
    with psycopg2.connect(
        user=os.environ["USER_NAME"],
        password=os.environ["USER_PASSWORD"],
        host=os.environ["USER_HOST"],
        port=os.environ["USER_PORT"],
        database=os.environ["USER_DATABASE"]
    ) as conn:
        return conn


@app.get("/user/{id}", summary="Get user by id")
def get_user(id: int, db: connection = Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            """
            SELECT *
            FROM "user"
            WHERE id= %(id)s
            """,
            {'id': id}
        )
        return cursor.fetchall()


@app.get("/post/{id}", summary="Get post by id")
def get_post_by_id(id: int, db: connection = Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            """
            SELECT *
            FROM post
            WHERE id= %(id)s
            """,
            {'id': id}
        )
        result = cursor.fetchall()
        if not result:
            raise HTTPException(404, 'Error 404')
        else:
            return result


# Для доступа к переменным окружения
# вызываем метод load_dotenv из библиотеки dotenv


if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app)
