from fastapi import FastAPI

app = FastAPI()

@app.get("/rangga/")
def read_rangga():
    return {"message" : "Hello, Rangga!"}