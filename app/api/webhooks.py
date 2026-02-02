from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.models.ticket import Ticket
from app.models.event import Event
import json

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

@router.post("/vendor")
def vendor_webhook(payload: dict, session: Session = Depends(get_session)):
    ticket = Ticket(
        external_id=payload["ticket_id"],
        status=payload["status"],
        priority=payload["priority"],
        description=payload["description"]
    )
    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    event = Event(
        ticket_id=ticket.id,
        payload=json.dumps(payload)
    )
    session.add(event)
    session.commit()

    return {"message": "Webhook processed"}
