from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse

app = FastAPI()

def _extract_validation_token(request: Request):
    for k, v in request.query_params.multi_items():
        if k.lower() == "validationtoken":
            return v
    return None

@app.get("/graph/notifications")
async def graph_validation(request: Request):
    token = _extract_validation_token(request)
    if token:
        print("Validation hit with token:", token)
        # Explicit text/plain — super safe for Graph
        return Response(content=token, media_type="text/plain", status_code=200)
    return Response(content="OK", media_type="text/plain", status_code=200)

@app.get("/graph/notifications/")
async def graph_validation_alt(request: Request):
    return await graph_validation(request)

@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    # Be defensive: body might be empty or not JSON
    try:
        body = await request.body()
        payload = (await request.json()) if body else {}
    except Exception:
        payload = {}
    print("NOTIFICATION:", payload)  # shows in Render logs
    # acknowledge immediately
    return JSONResponse({"received": True})
