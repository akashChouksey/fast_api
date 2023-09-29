from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
import schemas, models, database
from repository import dbBlog
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get('', status_code=200, response_model=List[schemas.ShowBlogs])
def blog(db: Session = Depends(database.get_db)):
    return dbBlog.get_all(db)


@router.get('/{id}',response_model=schemas.ShowBlogs)
def show(blog_id, db: Session = Depends(database.get_db)):
    return dbBlog.select_one(db, blog_id)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return dbBlog.create(db, request)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(blog_id: int, requests: schemas.Blog, db: Session = Depends(database.get_db)):
    return dbBlog.update(db, blog_id, requests)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(blog_id: int, db: Session = Depends(database.get_db)):
    return dbBlog.destroy(db, blog_id)
