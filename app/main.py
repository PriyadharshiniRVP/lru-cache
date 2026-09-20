from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title= "LRU Cache Service",
    description= "An project using doubly linked list and a dictionary to understand the LRU Caches",
    version="1.0.0"
)

app.include_router(router)

def root():
    return {"message" : "The LRU cache service is working visit /docs to try it out"}
