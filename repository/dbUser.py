import models, schemas
from sqlalchemy.orm import Session
from hashing import Hash


def create(db: Session, request: schemas.CreateUser):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(db: Session):
    return db.query(models.User).all()
