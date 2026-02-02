from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from pydantic import BaseModel

from app.db.session import get_session
from app.models.ticket import Ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# =========================
# DTOs
# =========================

class TicketCreate(BaseModel):
    external_id: str
    status: str
    priority: str
    description: str


class TicketUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    description: Optional[str] = None


# =========================
# Endpoints
# =========================

@router.get("/")
def list_tickets(session: Session = Depends(get_session)):
    """
    List all tickets
    """
    statement = select(Ticket)
    tickets = session.exec(statement).all()
    return tickets


@router.post("/")
def create_ticket(
        ticket: TicketCreate,
        session: Session = Depends(get_session)
):
    """
    Create a new ticket
    """
    db_ticket = Ticket(
        external_id=ticket.external_id,
        status=ticket.status,
        priority=ticket.priority,
        description=ticket.description
    )

    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)

    return db_ticket


@router.patch("/external/{external_id}")
def update_ticket_by_external_id(
        external_id: str,
        ticket_update: TicketUpdate,
        session: Session = Depends(get_session)
):
    """
    Update ticket using external_id (used by n8n workflows)
    """
    statement = select(Ticket).where(Ticket.external_id == external_id)
    ticket = session.exec(statement).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    for field, value in ticket_update.dict(exclude_unset=True).items():
        setattr(ticket, field, value)

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return ticket


@router.patch("/{ticket_id}")
def update_ticket_by_id(
        ticket_id: int,
        ticket_update: TicketUpdate,
        session: Session = Depends(get_session)
):
    """
    Update ticket using internal ID
    """
    ticket = session.get(Ticket, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    for field, value in ticket_update.dict(exclude_unset=True).items():
        setattr(ticket, field, value)

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return ticket
