from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from ai_tutor_bot.agents.tutor_agent import handle_query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to AI Tutor on Vercel!"}

@app.post("/ask/")
async def ask(request: Request):
    data = await request.json()
    query = data.get("query")
    try:
        answer = handle_query(query)
        return JSONResponse(content={"response": answer})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})