from fastapi import FastAPI
from credscore.service.app import app  # import your FastAPI app from the package

# Optional sanity endpoint
@app.get("/space_health")
async def space_health():
    return {"ok": True, "source": "space"}
