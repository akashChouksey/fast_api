from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from repository import dbUser

import database
import schemas

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.CreateUser, db: Session = Depends(database.get_db)):
    return dbUser.create(db, request)


@router.get('', status_code=200, response_model=List[schemas.User])
def user(db: Session = Depends(database.get_db)):
    return dbUser.get(db)
