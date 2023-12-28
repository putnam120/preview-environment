from fastapi import FastAPI
from pydantic import BaseModel
import uuid

class Data(BaseModel):
    id: str
    information: dict[str, str]

app = FastAPI()

@app.get("/", response_model=Data)
async def root() -> Data:
    return Data(id=uuid.uuid4().hex, information={"message": "Hello"})
