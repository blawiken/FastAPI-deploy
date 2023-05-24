from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Apps')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/apps/', response_model=schemas.App)
def create_app(app: schemas.AppCreate, db: Session = Depends(get_db)):
    return crud.create_app(db, app)


@app.get('/apps/', response_model=List[schemas.App])
def get_apps(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    apps = crud.get_apps(db, skip, limit)
    return apps


@app.get('/app/{app_id}', response_model=schemas.App)
def get_app(app_id: int, db: Session = Depends(get_db)):
    db_app = crud.get_app(db, app_id)
    if db_app is None:
        raise HTTPException(
            status_code=404,
            detail='App not found'
        )
    return db_app
