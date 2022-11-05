import uvicorn
from fastapi import FastAPI
import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status, HTTPException

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags = ["Root"])
async def profile():
    return {
       "slackUsername": "rector", 
       "backend": True, 
       "age": 24, 
       "bio": "I am nothing but pencil in the hands of the creator",
        }
    
@app.post("/arithmetics/", response_model=models.OutputModel)
async def arithmetics(data: models.InputModel):
    request_data = data.dict()
    operation_type = request_data['operation_type']
    x = request_data['x']
    y = request_data['y']

    operations = ['addition', 'subtraction', 'multiplication']

    if operation_type in operations:
        if operation_type == 'addition':
            result = x + y
        
        elif operation_type == 'subtraction':
            result = x - y

        else:
            result = x * y

        response = {
            "slackUsername": "rector",
            "result": result,
            "operation_type": operation_type
        }

        return response
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, details='Invalid operation type')
    




