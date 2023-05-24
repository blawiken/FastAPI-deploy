from sqlalchemy import Column, String, Integer

from .database import Base


class App(Base):
    __tablename__ = 'apps'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    text = Column(String)
