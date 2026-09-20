from app.cache import LRU_Cache


#  testing the get and put operation
def test_put_and_get():
    c = LRU_Cache(2)
    c.put(1,100)
    assert c.get(1) == 100
    
# testing if the function returns none for the key which doesn't exist   
def test_miss_returns():
    c = LRU_Cache(2)
    assert c.get(99) == None
    
    
# test if the capacity is exceeded the cache get removed    
def test_eviction():
    c = LRU_Cache(2)
    
    c.put(1,100)
    c.put(2,800)
    c.put(4,900)
    
    assert c.get(1) is None
    assert c.get(2) == 800
    assert c.get(4) == 900

# chech if the remove the least_recently used cache works    
def test_recently_used_survives():
    c = LRU_Cache(2)
    c.put(1,100)
    c.put(9,300)
    c.get(1)
    c.put(12,800)
    
    assert c.get(1) == 100
    assert c.get(2) is None

# check if the updation of the values works    
def test_update_works(): 
    c=LRU_Cache(2)
    c.put(9,99)
    c.put(9,29)
    assert c.get(9) == 29

# check if the delete function works    
def test_delete():   
    c = LRU_Cache(2)
    c.put(1,100)
    assert c.delete(1) is True
    assert c.get(1) is None
    assert c.delete(2) is False
 
# check if the stats are correct    
def test_stats():
    c=LRU_Cache(2)
    c.put(1,100)
    c.get(1)
    c.get(2)
    
    s=c.stats()
    assert s["hits"] == 1
    assert s["misses"] == 1
    assert s["total_req"] == 2
    assert s["current_size"] == 1
    assert s["capacity"] == 2
    
    
                    

     
        
 
    

    
     
        
    
    