from fastapi import APIRouter, HTTPException
from error import Duplicate, Missing

from model.explorer import Explorer
import service.explorer as service

router = APIRouter(prefix="/explorer")

@router.get("")
@router.get("/")
def get_all() -> list[Explorer] | None :
    return service.get_all()

@router.get("/{name}")
@router.get("/{name}/")
def get_one(name) -> Explorer | None:
    try:
       return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    
@router.patch("/{name}")
@router.patch("/{name}/")
def modify(name, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
        
@router.put("/{name}")
@router.put("/{name}/")
def replace(name, explorer: Explorer) -> Explorer:
    try:
        return service.replace(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
     
@router.delete("/{name}", status_code=204)
@router.delete("/{name}/", status_code=204)
def delete(name: str):
    try:
        return None
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
     