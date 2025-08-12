from fastapi import FastAPI, Request, Query
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/graph/notifications")
async def graph_validation(
    request: Request,
    validationToken: str | None = Query(default=None, alias="validationToken"),
    validationtoken: str | None = Query(default=None, alias="validationtoken"),
):
    # Accept both casings; echo *raw token* as plain text
    token = validationToken or validationtoken
    if token:
        print("Validation hit with token:", token)  # check Render logs
        return PlainTextResponse(token, status_code=200)
    return PlainTextResponse("OK", status_code=200)

@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    payload = await request.json()
    print("NOTIFICATION:", payload)  # shows in Render logs
    return JSONResponse({"received": True})
