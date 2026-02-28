from fastapi import FastAPI

app = FastAPI(title="Invest Agent API")

@app.get("/health")
def health():
    return {"status": "ok"}