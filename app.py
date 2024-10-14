from fastapi import FastAPI
from api.router import router

app = FastAPI()

app.include_router(router)

@app.get("/") 
def read_root():
    return {"message": "GS1-128 esta corriendo en el API!!"}
