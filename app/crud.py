from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email, password):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


def create_task(db: Session, task, user_id):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def delete_task(db: Session, task_id):
    task = db.query(models.Task).get(task_id)
    db.delete(task)
    db.commit()