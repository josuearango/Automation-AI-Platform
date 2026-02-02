from fastapi import FastAPI

app = FastAPI(title="Automation & AI Integration Platform")

@app.get("/health")
def health():
    return {"status": "ok"}
