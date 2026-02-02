from fastapi import APIRouter, HTTPException
from app.core.external_client import fetch_external_status

router = APIRouter(prefix="/integrations", tags=["Integrations"])


@router.get("/external-status")
async def external_status():
    try:
        return await fetch_external_status()
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="External service unavailable"
        )
