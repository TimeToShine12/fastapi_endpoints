from fastapi import FastAPI, Depends
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


@app.get("/user")
def get_user(id: int, limit: int = 10, db: connection = Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            """
            SELECT *
            FROM "user"
            WHERE id= %(id)s
            LIMIT %(limit)s
            """,
            {'limit': limit, 'id': id}
        )
        return cursor.fetchall()

# Для доступа к переменным окружения
# вызываем метод load_dotenv из библиотеки dotenv
if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app)
