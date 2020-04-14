class LRUCache:
    def __init__(self,capacity):
        self.cache = []
        self.capacity = 4
    def put(self,item):
        if item not in self.cache:
            if(self.cache.__len__()<self.capacity):
                self.cache.append(item)
            else:
                self.cache.pop(0)
                self.cache.append(item)        
        else:
            self.cache.append(self.cache.pop(self.cache.index(item)))
    def get(self):
        return self.cache[0]
    def get_cache(self):
        return self.cache
