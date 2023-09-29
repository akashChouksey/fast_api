import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog


def create(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, owner_id=request.owner_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def select_one(db: Session, blog_id: int):
    data = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found!")
    return data


def update(db: Session, blog_id: int, requests: schemas.Blog):
    blog_data = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog_data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found!")
    blog_data.update(requests.dict())
    db.commit()
    return 'updated'


def destroy(db: Session, blog_id: int):
    blog_data = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog_data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found!")
    blog_data.delete()
    db.commit()
    return 'done'
