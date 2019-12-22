from datetime import datetime

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class Players(BaseModel):
    id: int
    title: str
    price: int
    description: str = None

playerGlobal = [{
	"id":0,
	"name": "vova",
	"game":"cs go"
},
{
	"id":1,
	"name": "vanya",
	"game":"dota"
},
{
	"id":2,
	"name": "mykola",
	"game":"civilization 6"
}]

@app.get("/")
def get():
    return playerGlobal

@app.post("/create")
async def create(players: Players):
    jsonData = jsonable_encoder(players)
    playerGlobal.append(jsonData)
    return playerGlobal

@app.delete('/delete/{id}')
def delete(id: str):   
    return playerGlobal.pop(int(id)-1)

@app.put('/update/{id}')
def update(players: Players, id: str):
    playerGlobal[int(id)-1] = players
    return playerGlobal[int(id)-1]