

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from model_helper import predict
import shutil
import os

app = FastAPI(title="Vehicle Damage Detection API")

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Save uploaded image to temp location
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Call prediction
        prediction = predict(file_path)

        # Delete temp file
        os.remove(file_path)

        return JSONResponse(content={"prediction": prediction})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
