from fastapi import FastAPI
from domain.user import userRouter

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

app.include_router(userRouter.router)