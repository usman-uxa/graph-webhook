from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/graph/notifications")
async def graph_validation(validationToken: str | None = None):
    # Microsoft Graph sends GET ?validationToken=...
    if validationToken:
        return PlainTextResponse(validationToken, status_code=200)
    return PlainTextResponse("OK", status_code=200)

@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    payload = await request.json()
    # For now just acknowledge receipt
    return JSONResponse({"received": True, "value": payload.get("value", [])})
