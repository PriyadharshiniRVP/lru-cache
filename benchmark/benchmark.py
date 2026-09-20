import random
import httpx


BASE_URL = "http://127.0.0.1:8000"
TOTAL_REQUESTS = 500
KEY_RANGE = 20

def main():
    with httpx.Client(base_url=BASE_URL) as client:
        for i in range(TOTAL_REQUESTS):
            key = random.randint(1, KEY_RANGE)
            if random.random() < 0.7:
                client.get(f"/cache/{key}")
            else:
                client.post("/cache" , json={"key":key , "value" : key*10})
        
        stats = client.get("/cache-stats").json()
        print("Benchmark-results")
        print(f"Key-Range : {KEY_RANGE}")
        print(f"Total Requests : {TOTAL_REQUESTS}")
        
        for k,v in stats.items():
            print (f"{k} : {v}")
            
if  __name__ == "__main__":
    main()
    
    
          
            
            
                  
                
                
                