from fastapi import FastAPI, Request
from joblib import load, dump
from starlette.responses import FileResponse 
from fastapi.testclient import TestClient
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory="./app/templates")

# irisSavedFile = 'irisSavedModel.joblib'
# clfUploaded = load(irisSavedFile)


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
