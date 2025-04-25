# server_app.py
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

API_KEY = "my-secret-key"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataInput(BaseModel):
    data: str

def verify_api_key(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = auth.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return True

@app.post("/process")
def process_data(input_data: DataInput, authorized: bool = Depends(verify_api_key)):
    # Do some processing with input_data.data
    result = input_data.data.upper()  # Placeholder logic
    return {"result": result}
