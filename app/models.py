from pydantic import BaseModel

class cacheItem(BaseModel):
    key : int
    value : int


class cacheResponse(BaseModel):
    key : int
    value : int
    
class statsResponse(BaseModel):
    
    hits : int
    misses : int
    total_req : int
    hit_rate_percent : float
    current_size : int
    capacity : int
    
        
        