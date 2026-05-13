from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "Lala AI Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": f"You said: {req.prompt}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8099)