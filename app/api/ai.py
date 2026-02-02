from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI"])


class AnalyzeRequest(BaseModel):
    ticket_id: str
    text: str


@router.post("/analyze")
def analyze_ticket(payload: AnalyzeRequest):
    # Mock AI logic
    sentiment = "negative" if "critical" in payload.text.lower() else "neutral"
    urgency = "high" if sentiment == "negative" else "normal"

    return {
        "ticket_id": payload.ticket_id,
        "sentiment": sentiment,
        "urgency": urgency,
        "summary": f"AI analysis completed for ticket {payload.ticket_id}"
    }
