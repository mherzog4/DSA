# Heaps / priority queue

## Heap properties

### Priority queue
Regular queues - FIFO

You can base the queue based on a priority of the values

there are two variations - minimum priority & max priority


Heap and priority ques are the same thing

### Structure property

a binary heap is a binary tree that is considered a complete binary tree

that means you have a tree where every single level of the tree is going to be completely full (except the last level)

### Order property

For min heap

the whole point is to be finding the min or max value really quickly and easy

you want the min of all the nodes to be at the root - O(1)

recevrusively you want every value of the left subtree and right tree to be greater than the root node

under the hood arrays are being used

put the root node at index 1 - the main reason we skip index 0 is for the math to work out correctly   

leftChild = 2 * 1
rightChild = 2 * 1 + 1
parent = i/2



## Push and pop

### Pushing

Inserting into a heap/priortiy queue = Push

if the parent is larger than the child then you swap

``` python
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

    # Percolate up
    while self.heap[1] < self.heap[ i // 2]:
        tmp = self.heap[i]
        self.heap[i] = self.heap[i // 2]
        self.heap[i // 2] = tmp
        i = 1 // 2
```

O(logn)

### Pop

more complicated than inserting

to get pop to work and maintain the structure you have to remove root node and replace it with the last node in the tree to maintain the order property

and then instead of percoluating up, you percolate down

if the parent is bigger than the child, then swap



``` python
 def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]   
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and 
            self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

```


## Heapify

can get min/max in constant time 

an advantage to heaps is actually hwo you can build them comapred to BSTs

for heaps you can use a special algo (heapify) - the idea is that you can take the values of an array and turn them into a heap that satisifies the properties of a heap in O(n) time

the order porperty is recrusive

``` python
import heapq

# Min Heap
class Heap:
    # ... not showing push, pop to save space.
    
    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
```

percolating down is more efficient than percalating up

can get min and max in costant time O(1)

