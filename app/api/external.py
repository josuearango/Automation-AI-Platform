from fastapi import APIRouter, Header, HTTPException

router = APIRouter(prefix="/external-api", tags=["External API"])

FAKE_API_KEY = "secret-api-key"


@router.get("/status")
def get_external_status(x_api_key: str = Header(None)):
    if x_api_key != FAKE_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "service": "fake-vendor",
        "status": "operational"
    }
