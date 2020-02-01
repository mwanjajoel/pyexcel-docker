from fastapi import FastAPI, File, UploadFile 
import pyexcel as p
from pyexcel_xlsx import get_data
import requests

app = FastAPI()


@app.get("/")
async def welcome():
    return {"PyExcel": "You have arrived!"}

@app.get("/upload")
async def file_upload():
    return '''
    <!doctype html>
    <title>Upload an excel file here</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz, xls, xlsx only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
     return {"filename": file.filename}



