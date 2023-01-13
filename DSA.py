# Python for completing DSA

## Variables are dynamcily typed 

n = 0 
print('n =', n)

n = "abc"
print('n =', n)

## Multiple assignments

n, m = 0, "abc"

### Increment

n = n  + 1
n+= 1

## None is null (absence of value)
n = 4
n = None
print("n =", n)

## If statements dont need parens or curly braces
n = 1 
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
print("n =", n)

## Parens needed for multi-line conditions
### and = &&
### or = ||
n, m = 1,2
if ((n > 2 and
    n != m) or n == m):
    n += 1
print("n =", n, "m = ", m)

## While loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

## Looping from i = 0 to i = 4
for i in range(5):
    print("looping =", i)

## Looping from i = 2 to i = 5
for i in range(2,6):
    print(i)

## Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

## Division is decimal by default
print(5 / 2)

## Double slash rounds down
print(5 // 2)

## CAREFUL: Most languages round towards 0 by default so negative numbers will round down
print(-3 // 2)

## A workaround for rounding towards zero is to use decimal divison and then convert to int
print(int(-3 / 2 ))

## Modding is similar to most languages
print(10 % 3)

### Except for negative values
print(-10 % 3)

### To be consitent with other languages modulo
import math
print(math.fmod(-10, 3))

## More math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

## Max / Min int
float("inf")
float("-inf")

## Python numbers are infinite so they never overflow
import math
print(math.pow(2, 200))

### But still less than infinity
print(math.pow(2, 200) < float("inf"))

## Arrays (called lists in python)
arr = [1,2,3]
print(arr)

## Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

## Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

## Careful: -1 is not out of bounds, its the last value
arr = [1, 2, 3]
print(arr[-1])

## Indexing -2 is the second to last value, etc
print(arr[-2])

## Sublists (aka slicing)
arr = [1,2,3,4]
print(arr[1:3])

## similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

## Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

## Loop through arrays
nums = [1, 2, 3]

### using index
for i in range(len(nums)):
    print(nums[i])

### Without index
for n in nums:
    print(n)

### With index and value
for i, n in enumerate(nums):
    print(i, n)

## Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2, in zip(nums1, nums2):
    print(n1, n2)

## Reverse

nums = [1, 2, 3]
nums.reverse()
print(nums)

## Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

## Sorting strings
arr = ["bob", "alice", "fred", "doe"]
arr.sort()
print(arr)

### Custom sort (by length of string)

arr.sort(key=lambda x: len(x))
print(arr)

## List comprehension

arr = [i+i for i in range(5)]
print(arr)

## 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)

## Strings are similar to arrays
s = "abc"
print(s[0:2])

### So this creates a new string

s += "def"
print(s)

## Valid numeric strings can be converted
print(int("123") + int("123"))

### Add numbers can be converted to strings

print(str(123) + str(123))

## Combine a list of strings (with an empty string delimitor)

strings = ["ab", "cd", "ef"]
print("".join(strings))

## Queues (double ended quue)

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

## HashSet

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

## List to set

print(set([1, 2, 3]))

### Set comprehension
mySet = { i for i in range(5) }
print(mySet)

## Hashmap (aka dictionary)
myMap = {}
myMap["alice"] = 99
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = { "alice": 90, "bob": 70 }
print(myMap)

## Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)

## Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.items():
    print(key, val)

## Tuples are like arrays but immuatable

tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

## Heaps
import heapq

### under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

#### min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

## No max heaps by default, work around is to use min heap and multiply by -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

### Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

### Build heap from initial values

arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

## Functions

def myFunc(n, m):
    return n * m

print(myFunc(3,4))

## Nested functions have access to outer variables

def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

## can modify objects but not reassign unless using nonlocal keyword

def double(arr, val):
    def helper():
        # modifying array works
        for i, n in enumerate(arr):
            arr[1] *= 2

        # will only modify val in the helper scpoe 
        # val *= 2
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

## Class

class myClass:
    # constructor
    def __init__(self, nums):
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


