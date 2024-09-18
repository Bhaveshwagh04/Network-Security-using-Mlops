import os
import sys

import pymongo

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.ml_utils.model.estimator import ModelResolver
from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR

from networksecurity.utils.main_utils.utils import load_object

def set_env_variable(env_file_path):
    pass

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        #train_pipeline = TrainingPipeline()
        #if train_pipeline.is_pipeline_running:
            #return Response("Training pipeline is already running.")
        #train_pipeline.run_pipeline()
        #return Response("Training successful !!")
        pass
    except Exception as e:
            raise NetworkSecurityException(e,sys)


@app.post("/predict")
async def predict_route(request: Request,file: UploadFile = File(...)):
    try:
        pass
    except Exception as e:
            raise NetworkSecurityException(e,sys)
        
def main():
    try:
        training_pipeline = TrainingPipeline()
        model = training_pipeline.run_pipeline(model_dir=SAVED_MODEL_DIR) 
    except Exception as e:
            raise NetworkSecurityException(e,sys)

    
if __name__=="__main__":
    main()
    set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT)