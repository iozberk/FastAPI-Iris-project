from fastapi import FastAPI, Request
from joblib import load, dump
from starlette.responses import FileResponse 
from fastapi.testclient import TestClient
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import numpy as np
from sklearn.datasets import load_iris
dataSet = load_iris()
labelsNames = list(dataSet.target_names)

app = FastAPI()

templates = Jinja2Templates(directory="./app/templates")

irisSavedFile = 'irisSavedModel.joblib'
clfUploaded = load(irisSavedFile)


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predict")
async def make_prediction(request: Request, L1:float, W1:float,
                          L2:float, W2:float):
    testData= np.array([L1,W1,L2,W2]).reshape(-1,4)
    probalities = clfUploaded.predict_proba(testData)[0]
    predicted = np.argmax(probalities)
    probabilty= probalities[predicted]
    predicted = labelsNames [predicted]
    return templates.TemplateResponse("prediction.html",
                                      {"request": request,
                                       "probalities": probalities,
                                      "predicted": predicted,
                                      "probabilty": probabilty}  )
