from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.ticket import Ticket
from app.models.event import Event
import json
import httpx

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/vendor-ticket"


@router.post("/vendor")
def vendor_webhook(payload: dict, session: Session = Depends(get_session)):
    # 1. Idempotency: check if ticket already exists
    statement = select(Ticket).where(Ticket.external_id == payload["ticket_id"])
    ticket = session.exec(statement).first()

    if not ticket:
        ticket = Ticket(
            external_id=payload["ticket_id"],
            status=payload["status"],
            priority=payload["priority"],
            description=payload["description"]
        )
        session.add(ticket)
        session.commit()
        session.refresh(ticket)

    # 2. Store event
    event = Event(
        ticket_id=ticket.id,
        payload=json.dumps(payload)
    )
    session.add(event)
    session.commit()

    # 3. Trigger n8n AUTOMATICALLY
    with httpx.Client(timeout=5) as client:
        client.post(
            N8N_WEBHOOK_URL,
            json={
                "ticket_id": ticket.external_id,
                "status": ticket.status,
                "priority": ticket.priority,
                "description": ticket.description
            }
        )

    return {
        "message": "Webhook processed and n8n triggered",
        "external_id": ticket.external_id,
        "ticket_db_id": ticket.id
    }
