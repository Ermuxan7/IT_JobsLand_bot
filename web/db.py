from databases import Database
import uuid, sqlalchemy
from sqlalchemy import Table, Column, Text, String, Integer, TIMESTAMP, MetaData, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from bot.config import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()

vacancies = Table(
    "vacancies",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", BigInteger, nullable=False),
    Column("company", String, nullable=False),          
    Column("position", String, nullable=False),          
    Column("requirements", Text, nullable=False),          
    Column("address", String, nullable=False),          
    Column("working_time", String, nullable=False),          
    Column("salary", String, nullable=False),          
    Column("contacts", String, nullable=False),          
    Column("additional", Text, nullable=False),               
    Column("status", String, default="pending"),
    Column("created_at", TIMESTAMP, server_default=sqlalchemy.func.now()),
    Column("updated_at", TIMESTAMP, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
)

resumes = Table(
    "resumes",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", BigInteger, nullable=False),
    Column("full_name", String, nullable=False),
    Column("profession", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("address", String, nullable=False),
    Column("skills", Text, nullable=False),
    Column("experience", String, nullable=False),
    Column("portfolio", Text),
    Column("salary", Text, nullable=False),
    Column("goal", Text, nullable=False),
    Column("contacts", String, nullable=False),
    Column("status", String, default="pending"),
    Column("created_at", TIMESTAMP, server_default=sqlalchemy.func.now()),
    Column("updated_at", TIMESTAMP, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
)

projects = Table(
    "projects",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", BigInteger, nullable=False),
    Column("specialist", String, nullable=False),
    Column("task", String, nullable=False),
    Column("budget", String, nullable=False),
    Column("additional", Text, nullable=False),
    Column("contacts", String, nullable=False),
    Column("status", String, default="pending"),
    Column("created_at", TIMESTAMP, server_default=sqlalchemy.func.now()),
    Column("updated_at", TIMESTAMP, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)