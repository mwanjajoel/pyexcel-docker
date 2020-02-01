from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def welcome():
    return {"PyExcel": "You have arrived!"}

@app.get("/items/{item_id}")
async def get_items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

