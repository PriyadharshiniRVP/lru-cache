class Node:
    
    ## Initializing the doubly linked list
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
        
class LRU_Cache:
    ## Initialising a Dict
    
    def __init__(self,capacity:int):
        
        self.capacity = capacity
        self.cache = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.hits=0
        self.misses=0
    
    # removing a node    
    def remove(self,node :Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev= prev_node
        
    # adding a node to recent  ; next to the head
    def addtofront(self,node:Node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # rendering the key and adding it to the recent aka next to the head    
    def get(self,key:int) :
        
        if key not in self.cache:
            self.misses+=1   # miss+1 if its not in key - it would help in testing stats
            return None
        node = self.cache[key]
        
        self.remove(node)  # since the key is saw , remove it from the current position
        self.addtofront(node) # add the key next to the head
         
        self.hits+=1 # since the key is seen increment the hits , same as miss, would help in the testing  stats
        return node.value
    
    # Putting the key inside the cache 
    def put(self,key:int , value:int):
        if key in self.cache:
            node = self.cache[key]  #if the the key already presents
            node.value = value # update the value of it with the new value
            self.remove(node) # since its recently checked , remove it from current position
            self.addtofront(node) # add it next to the head
        else:
            new_node = Node(key,value) # if not present in the cache , add a new node with the given key and value
            self.cache[key] = new_node
            
            self.addtofront(new_node) # add it next to the head
            if len(self.cache) > self.capacity: # if the size exceeds 
                lru_node = self.tail.prev # remove the least recently used one
                self.remove(lru_node) # remove it using the function we declared
                del self.cache[lru_node.key] # delete the key of it too
     
     # Deleting a particular node with its key            
    def delete(self , key:int):
        if key in self.cache:  # if the key is present
            node = self.cache[key] # node 's value by key
            self.remove(node) # remove the node from the linked-list
            del self.cache[key]   # remove the key from dict
            return True
        return False
    
    
    # Finding the Stats of the caching
    def stats(self):  
        total = self.hits + self.misses
        hit_rate = (self.hits / total*100) if total > 0 else 0
        return {
            "hits": self.hits,
            "misses": self.misses,
            "total_req": total,
            "hit_rate_percent": round(hit_rate,2),
            "current_size" : len(self.cache),
            "capacity" : self.capacity
            
        }
        
        
    # returning the current cache list
    def caches(self):
        result = []
        current = self.head.next
        
        while current != self.tail:
            result.append({"key":current.key , "value":current.value})
            current = current.next
        return result    
            
                       
                
           
        
            
        
        
        
        
            
        
        