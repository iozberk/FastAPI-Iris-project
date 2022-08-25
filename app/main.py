from fastapi import FastAPI
from joblib import load, dump
from starlette.responses import FileResponse 
from fastapi.testclient import TestClient



app = FastAPI()
# irisSavedFile = 'irisSavedModel.joblib'
# clfUploaded = load(irisSavedFile)

@app.get("/")
def root():
    return FileResponse('index.html')
