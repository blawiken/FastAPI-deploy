from pydantic import BaseModel


class AppBase(BaseModel):
    title: str
    text: str | None = None


class AppCreate(AppBase):
    pass


class App(AppBase):
    id: int
    
    class Config:
        orm_mode = True
        