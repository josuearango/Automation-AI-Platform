from fastapi import FastAPI
from app.api.webhooks import router as webhook_router
from app.api.tickets import router as tickets_router
from app.api.ai import router as ai_router

app = FastAPI(title="Automation & AI Integration Platform")

app.include_router(webhook_router)
app.include_router(tickets_router)
app.include_router(ai_router)

@app.get("/health")
def health():
    return {"status": "ok"}
