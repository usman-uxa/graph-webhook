from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Hello from Graph webhook"}

@app.get("/graph/notifications")
@app.post("/graph/notifications")
async def graph_notifications(request: Request):
    token = request.query_params.get("validationToken")
    if token:
        print(f"Validation hit with token: {token}")
        return PlainTextResponse(content=token, status_code=200)

    try:
        payload = await request.json()
        print(f"Notification payload: {payload}")
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        payload = None

    return JSONResponse(content={"status": "ok"})

