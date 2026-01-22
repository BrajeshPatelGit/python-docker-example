from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hands on deck for git, vs code, docker, python, and fastapi!"}
