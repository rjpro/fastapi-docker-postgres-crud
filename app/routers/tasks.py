from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/tasks")


@router.post("/")
def create(task: schemas.TaskCreate,
           db: Session = Depends(get_db),
           user=Depends(get_current_user)):
    return crud.create_task(db, task, user.id)


@router.get("/")
def read(db: Session = Depends(get_db),
         user=Depends(get_current_user)):
    return crud.get_tasks(db, user.id)


@router.delete("/{task_id}")
def delete(task_id: int,
           db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return {"msg": "deleted"}