from fastapi import APIRouter
import psycopg2

from dbs_assignment.config import settings


router = APIRouter()


@router.get("/v1/status")
async def get_status_version():
    try:
        connected = psycopg2.connect(
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            dbname=settings.DATABASE_NAME,
        )

        with connected.cursor() as database_cursor:
            database_cursor.execute("SELECT version();")
            database_version = database_cursor.fetchone()
            connected.close()
            return {"version": database_version[0]}
    except Exception as e:
        print(e)
        exit(1)

