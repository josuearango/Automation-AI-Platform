from sqlmodel import SQLModel
from .session import engine
from app.models.ticket import Ticket
from app.models.event import Event

def init_db():
    SQLModel.metadata.create_all(engine)
