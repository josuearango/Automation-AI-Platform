from sqlmodel import SQLModel, Field
from datetime import datetime

class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ticket_id: int
    payload: str
    received_at: datetime = Field(default_factory=datetime.utcnow)
