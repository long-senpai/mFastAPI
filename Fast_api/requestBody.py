from fastapi import FastAPI, Query
from typing import Optional
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[str] = None
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): # khai báo dưới dạng parameter
    return {"item detail " : item}

#curl -X 'POST' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "long",
#   "description": "hello world",
#   "price": 12345,
#   "tax": "1"
# }'


### Request bd + path parameters
@app.put("/items/{item_id}")
async def requestBD_PathParam(item_id : int, item: Item):

    return {"id ": item_id, **item.dict()}
# Response body: 
# {
#   "id ": 5,
#   "name": "long",
#   "description": "hello",
#   "price": 11111,
#   "tax": "0123"
# }

### Request body + path + query parameters
@app.put("/items1/{item_id}")
async def requestBD_Path_queryParam(item_id : int, item: Item, q : str or None = None):
    data ={"id ": item_id, **item.dict()}
    if q :
        data.update({"q":q})
    return data

# Query parameter list / multiple values
from typing import List, Optional

@app.get("/items2/")
async def read_items(q: Optional[List[str]] = Query(None, max_length=200)):
    query_items = {"q": q}
    return query_items



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
