from __init__ import conn, curs
from model.creature import Creature

curs.execute("""create table if not exists creature(
    name text primary key,
    description text,
    country text,
    area text,
    aka text) """)

def row_to_model(row: tuple) -> Creature:
    (name, description, country, area, aka) = row
    return Creature(name, description, country, area, aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name= :name"
    params = {"name" : name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())

