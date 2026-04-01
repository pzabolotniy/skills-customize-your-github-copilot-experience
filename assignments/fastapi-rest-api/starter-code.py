# Starter code for FastAPI REST API assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# TODO: Implement CRUD endpoints for /items/
# - POST /items/
# - GET /items/
# - GET /items/{item_id}
# - PUT /items/{item_id}
# - DELETE /items/{item_id}
