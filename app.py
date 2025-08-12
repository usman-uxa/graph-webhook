from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

def _extract_validation_token(request: Request) -> str | None:
    # case-insensitive lookup for any key that equals 'validationtoken'
    for k, v in request.query_params.multi_items():
        if k.lower() == "validationtoken":
            return v
    return None

@app.get("/graph/notifications")
async def graph_validation(request: Request):
    token = _extract_validation_token(request)
    if token:
        print("Validation hit with token:", token)
        return PlainTextResponse(token, status_code=200)  # raw token, no quotes
    return PlainTextResponse("OK", status_code=200)

# also handle the trailing-slash variant, just in case
@app.get("/graph/notifications/")
async def graph_validation_alt(request: Request):
    return await graph_validation(request)

@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    payload = await request.json()
    print("NOTIFICATION:", payload)   # visible in Render logs
    return JSONResponse({"received": True})
