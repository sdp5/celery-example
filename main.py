# main.py - FastAPI Integration

from fastapi import FastAPI
from workflow import process_documents  # Import your workflow function
from celery_config import celery_app

app = FastAPI()

@app.post("/process/")
async def process_endpoint(blob_path: str):
    result = process_documents(blob_path)
    return {"task_id": result.id}

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.state == 'PENDING':
        return {"status": "Pending..."}
    elif result.state == 'SUCCESS':
        return {"status": "Completed", "result": result.result}
    elif result.state == 'FAILURE':
        return {"status": "Failed", "result": str(result.result)}
    else:
        return {"status": result.state}
