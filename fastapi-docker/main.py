from fastapi import FastAPI

app = FastAPI()  # <-- this must exist

@app.get("/")
def read_root():
    return {"message": "Hello World"}
