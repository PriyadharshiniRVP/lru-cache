from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title= "LRU Cache Service",
    description= "A from-scratch LRU cache implemented with a hash map and doubly linked list, exposed as a REST API.",
    version="1.0.0"
)

app.include_router(router)

def root():
    return {"message" : "The LRU cache service is working visit /docs to try it out"}
