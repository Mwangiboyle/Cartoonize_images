from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return ("Your api is running successful")

