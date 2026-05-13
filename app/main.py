from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": run_agent(req.prompt)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8099)