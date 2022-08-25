from fastapi import FastAPI
from joblib import load, dump


app = FastAPI()

irisSavedFile = 'irisSavedModel.joblib'
clfUploaded = load(irisSavedFile)

@app.get("/")
def root():
    return FileResponse('index.html')
