from fastapi import FastAPI

from app.api.webhooks import router as webhook_router
from app.api.tickets import router as tickets_router
from app.api.ai import router as ai_router
from app.api.external import router as external_router
from app.api.integrations import router as integrations_router

app = FastAPI(title="Automation & AI Integration Platform")


# =========================
# Routers
# =========================
app.include_router(webhook_router)
app.include_router(tickets_router)
app.include_router(ai_router)
app.include_router(external_router)
app.include_router(integrations_router)

# =========================
# Health check
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}
