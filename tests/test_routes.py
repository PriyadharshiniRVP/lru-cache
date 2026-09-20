from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/cache-items")
    assert r.status_code == 200
    
def test_post_and_get():  
    client.post("/cache" , json = {"key" : 10,"value" : 100})
    r = client.get("/cache/10")
    assert r.status_code == 200
    assert r.json() ==  {"key":10 , "value" :100}
    
    
def test_missing_key():
    r = client.get("/cache/9999")
    assert r.status_code == 404

def test_delete():
    client.post("/cache" , json = {"key" :20 ,"value": 400})
    r = client.delete("/cache/20")
    assert r.status_code == 200
    r = client.get("/cache/20")
    assert r.status_code == 404
    
def test_stats():
    r = client.get("/cache-stats")
    assert r.status_code == 200
    data = r.json()
    assert "hits" in data
    assert "misses" in data
    
        
            

        
    