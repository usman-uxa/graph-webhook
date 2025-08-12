from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/graph/notifications")
async def graph_validation(request: Request):
    # Accept both validationToken and validationtoken (Graph can send lowercase)
    qp = request.query_params
    token = qp.get("validationToken") or qp.get("validationtoken")
    if token:
        return PlainTextResponse(token, status_code=200)
    return PlainTextResponse("OK", status_code=200)

@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    payload = await request.json()
    return JSONResponse({"received": True})
