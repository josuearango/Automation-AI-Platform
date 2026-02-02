from sqlmodel import SQLModel, Field
from datetime import datetime

class Ticket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    external_id: str
    status: str
    priority: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
