from fastapi import FastAPI

app = FastAPI(title="NexConnect")

@app.get("/")
def root():
    return {"message": "Welcome to NexConnect!"}
