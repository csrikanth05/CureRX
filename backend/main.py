from fastapi import FastAPI
from llm import ask_model
import json, asyncio

app = FastAPI()

@app.get("/protein/{protein}")
async def protein(protein:str):
    raw = await asyncio.to_thread(asyncio.run, ask_model(protein))
    try:
        return json.loads(raw)
    except Exception:
        return {"error":"LLM parsing failed","raw":raw}
