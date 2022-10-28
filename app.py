import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags = ["Root"])
async def read_root():
    return {
       "slackUsername": "rector", 
       "backend": True, 
       "age": 24, 
       "bio": "I am nothing but pencil in the hands of the creator",
        }




