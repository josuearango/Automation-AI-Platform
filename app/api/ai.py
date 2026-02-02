from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI"])


# =========================
# Request schema
# =========================
class AnalyzeRequest(BaseModel):
    ticket_id: str
    text: str


# =========================
# AI Analyze Endpoint (Mock)
# =========================
@router.post("/analyze")
def analyze_ticket(payload: AnalyzeRequest):
    """
    Mock AI analysis endpoint.

    This simulates an AI service that evaluates a ticket's text
    and returns sentiment and urgency for automation decisions.
    """

    text_lower = payload.text.lower()

    sentiment = "negative" if "critical" in text_lower else "neutral"
    urgency = "high" if sentiment == "negative" else "normal"

    return {
        "ticket_id": payload.ticket_id,
        "sentiment": sentiment,
        "urgency": urgency,
        "summary": f"AI analysis completed for ticket {payload.ticket_id}"
    }
