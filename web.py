from fastapi import FastAPI

from model import Creature


app = FastAPI()
@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()

