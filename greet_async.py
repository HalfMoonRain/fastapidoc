import asyncio
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/hi')
async def greet():
    await asyncio.sleep(3)
    return "Hello, World?"

