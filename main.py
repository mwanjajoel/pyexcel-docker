from fastapi import FastAPI 
import pyexcel as p
from pyexcel_xlsx import get_data

app = FastAPI()


@app.get("/")
async def welcome():
    return {"PyExcel": "You have arrived!"}

@app.route("/upload", methods=['GET', 'POST'])
async def upload_file():
    return {"File":"Uploaded"}



