from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_NAME = 'sql_app.db'

SQLALCHEMY_DATABASE_URL = f"sqlite:///./database/{DATABASE_NAME}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db() -> None:
    try:
        db = open(f'database/{DATABASE_NAME}')
    except FileNotFoundError as e:
        Base.metadata.create_all(bind=engine)
    else:
        pass


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
