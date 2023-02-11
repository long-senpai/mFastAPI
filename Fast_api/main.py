from fastapi import FastAPI, Query
from typing import Optional
import uvicorn

app = FastAPI()
@app.get('/')
async def index():
    return {'hello' : {"test" : 1}}


@app.get('/blogs/{id}')
async def show(id):

    return {"Data": id}

###########################################################################################################
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}] 

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# query parameter 
# Push the parameter as default, and even add the parameter as optional
# assgin the type for parameters
## NOTE that optional only take string value and has the lengh < 50 characters

@app.get('/blog')
async def index(limit=10, published: bool = True, q : Optional[str] = None ):

    return {"Data": f'the limit number here is {limit}'} 

@app.get('/blog1')  # q: Optional[str] = Query(None, max_length=250)
async def index(limit=10, published: bool = True, q : Optional[str] = Query(None, max_length=250) ):

    return {"Data": f'the limit number here is {limit}'} 


## POST method to create something



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
