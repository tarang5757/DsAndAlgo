
class HashMap:
    def __init__(self):
        #with self you can access attributes and methods. its a instance of this class
        self.size = 10 #initial size
        self.slots = [[] for _ in range(self.size)] #List of slots to store key-value pairs

    def _hash(self, key):
        return hash(key) % self.size #hash function to determine the slot for a given key

    def add(self, key, value):
        slot = self._hash(key)
        for i, (k, v) in enumerate(self.slots[slot]):
            if k == key:
                self.slots[slot][i] = (key, value)
                return
        self.slots[slot].append((key,value))
    
    def get(self, key):
        slot = self._hash(key)
        for k, v in self.slots[slot]:
            if k == key:
                return v
        return None #not found
    
    def remove(self, key):
        slot = self._hash(key)
        for i, (k, v) in enumerate(self.slots[slot]):
            if k == key:
                del self.slots[slot[i]]
                return

    def display(self):
        for slot in self.slots:
            for k, v in slot:
                print(f"Key: {k}, Value: {v}")


#testing
hashmap = HashMap()

hashmap.add('apple', 3)
hashmap.add('banana', 6)
hashmap.add('orange', 4)

print(hashmap.get('orange')) #output: 3
hashmap.display()

    
    










