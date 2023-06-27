from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    print(SQLALCHEMY_DATABASE_URL)
    from app.models.user import User
    from app.models.interaction import Interaction
    with SessionLocal() as session:
        print(session.query(User).all())
        session.delete(User(name="Test", email="text@gmail.com"))
        session.commit()

        print(session.query(User).all())
        session.query(User).filter(User.name == "Test").delete()
        session.commit()

        print(session.query(User).all())