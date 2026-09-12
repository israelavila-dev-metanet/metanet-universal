import uvicorn
import json
import fastapi
from connec-mikrotis import MikrotikConnection
app = fastapi.FastAPI()

print("Starting the FastAPI application...")

def main():
    if uvicorn is None:
        raise RuntimeError("uvicorn is not installed. Please install it with: pip install uvicorn")
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

