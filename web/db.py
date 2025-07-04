from databases import Database
import sqlalchemy, os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

vacancies = sqlalchemy.Table(
    "vacancies",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.dialects.postgresql.UUID, primary_key=True),
    sqlalchemy.Column("message", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, default="pending"),
    sqlalchemy.Column("created_at", sqlalchemy.TIMESTAMP, server_default=sqlalchemy.func.now()),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)