from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def root():
    return {"Auth API with FastAPI is running"}
