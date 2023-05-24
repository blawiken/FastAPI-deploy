from sqlalchemy.orm import Session

from . import models, schemas


def get_app(db: Session, app_id: int):
    return db.query(models.App).filter(models.App.id == app_id).first()

def create_app(db: Session, app: schemas.AppCreate):
    db_app = models.App(
        title=app.title,
        text=app.text
    )
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_apps(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.App).offset(skip).limit(limit).all()
