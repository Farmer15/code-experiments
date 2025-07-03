from typing import Union

from fastapi import FastAPI

from tasks import add

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/add")
def run_add(x: int, y: int):
    result = add.delay(x, y)
    return {"task_id": result.id}
