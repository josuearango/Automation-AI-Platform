from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.ticket import Ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("/")
def get_tickets(session: Session = Depends(get_session)):
    statement = select(Ticket)
    tickets = session.exec(statement).all()
    return tickets


@router.post("/")
def create_ticket(ticket: Ticket, session: Session = Depends(get_session)):
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket
