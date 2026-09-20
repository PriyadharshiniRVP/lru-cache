from fastapi import APIRouter , HTTPException
from app.cache import LRU_Cache
from app.models import cacheItem , cacheResponse , statsResponse

router = APIRouter()


cache = LRU_Cache(6)


@router.get("/cache/{key}",response_model=cacheResponse)
def get_value(key:int):
    value = cache.get(key)
    if value is None:
        raise HTTPException(status_code=404 ,detail="key not found")
    return {
        "key" : key,
        "value" :value
    }
    
@router.post("/cache", response_model=cacheResponse) 
def put_value(item : cacheItem):
    cache.put(item.key , item.value) 
    return {
        "key" : item.key,
        "value" : item.value
    }  
    
@router.delete("/cache/{key}")
def delete_item(key : int):
    removed = cache.delete(key)   
    if not removed:
        raise HTTPException(status_code=404 ,detail="key not found")
    return {
        "message" : f"Key {key} deleted"
    }

@router.get("/cache-stats" , response_model=statsResponse)   
def get_stats() :
    return cache.stats()

@router.get("/cache-items")
def get_items():
    return {"cacheitems" : cache.caches()}

         
    
    