# Hashing

Hash sets and hash maps are very useful and common

## Hash usage

Sets are a set of values

Maps are a set of keys that are mapped to a different value (phone book example)

Primary focused on maps because they are more common and more complex

Treemaps Insert, Remove & Search:
O(logn)

Treemap: Inorder
O(n)

Hashmap: Insert, remove, Search
O(1) -> the average case time complexity

Hashmaps dont maintain any ordering

Hashmap: Inorder
O(nlogn)

``` python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    # If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1

```

## Hash Implementation

most likely uou wont be ask the implement a hashmap in a interview - the implementation can get complicated

under the hood a hashmap is implemented with an array

the index is mapped to the key value pair

even a empty hashmap is nonzero

Whats important is needing a way to convert the key into an integer - you do this by hashing

you can take any integer and mod it by the size by the array

hashing Collision - when key value pairs want to be set into the same index

to minimize collisions you keep track of the size and keys of the array

when hashmap because half full is typically when you re-size the array (like dynamic arrays)

when you resize the array you cant leave the values where they previously where - when you resize you take every key in the hashmap, you recompute with new size and move it where it should now be - call this rehashing the array

you can store a linked list of pairs to minimze collision - the downside is you have to add memory

Linked list approach is called chaining

Open addressing apporach - losely define where the index should go at

take the new index and add to it 



``` python
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

# Searching & Open addressing

    def get(self, key):
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

# Inserting 

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            index += 1
            index = index % self.capacity
    
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may 
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
    
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)

```