from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# GET endpoint with path parameter and optional query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "query": q
    }

# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# PUT request endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "item": item
    }