# Notes

## RAM

Before diving into what an array is, it is important to understand what a data structure is to begin with.

Simply put, data structures are a way to store data in an efficient manner inside the Random Access Memory, hereafter called "RAM". An array is a collection of ordered, contiguous group of elements. If we wanted to store three integers - 1, 3, 5 in our RAM, an array can be used. The question here is how does the computer store these numbers in the RAM if it only understands data in terms of bits - 0s and 1s. This requires understanding of the RAM. Computers these days have RAM in terms of gigabytes. In fact, the computer you are using to view this course might have 8 GB (109 bytes) of RAM. 1 byte = 8 bits. A bit is a 0 OR a 1.

Going back to our integers - 1, 3, 5, each one of them are stored in the RAM in terms of bytes, which gets converted to bits. Integers commonly occupy 4 bytes (32 bits) in memory. An address and a value gets associated with an integer upon storing it in RAM. An address is just a distinct location that each one of the values is stored at. Each value is stored contiguously in the RAM, just like an array.

Storing an integer array in RAM

Each integer takes 32 bits of space, 4 bytes, hence the addresses are 4 bytes apart.
Instead of integers, we could also store characters in an array.

Storing a character array into RAM. Each character takes 8 bits of space, 1 byte, hence the addresses are 1 byte apart.

Each character takes 8 bits of space, 1 byte, hence the addresses are 1 byte apart.
It does not really matter the size, or the type of value you store in the memory, as long as the address is incremented in accordance to the type of value being stored in the array. As software engineers, we don't need to worry about it since the operating system handles it for us. Still, it is good knowledge to possess.



## Static Arrays

To recall, arrays are a way to store data contiguously. In strictly typed languages like Java, C++, C# etc, arrays have to have an allocated size when initialized. This means that the size of the array cannot change once declared and once its capacity is reached, it can store no more values. Loosely typed languages such as Python and JavaScript do not have static arrays, which we will discuss in the next chapter.

Having said all that, let's go over the basic operations that can be performed on an array, their efficiency and usage. The most common operations are:

Reading
Deletion
Insertion
Reading from an array
For this example, we will be initializing an array of size 3 called myArray . Array elements are accessed using indices, which start at 00. So the first element resides at index 00, second at index 11 and so on.

// initialize myArray
myArray = [1,3,5]

// access an arbitrary element, where i is the index of the desired value
myArray[i]
As long as the index of an element is known, the access is instant. This is because each index of myArray is mapped to an address in the RAM. This is a single operation and in algorithm analysis, we say it runs in constant time, or O(1)O(1) put more formally. This means that regardless of the size of the array, the time taken to access our element will be unaffected - it will always be a single operation.

Traversing through an array
Reading all values from an array can be done using either a for loop or a while loop.


for i = 0 to myArray.size-1: 
   print(myArray[i])

// OR

i = 0
while i < myArray.size:
   print(myArray[i])
   i++
In the for loop, we only iterate until myArray.size-1 since that is the last accessible index of the array. The last index of the array is n - 1n−1 where nn is the length of the array. This makes sense because the size of our array is 3, meaning it can hold three elements and if we start our index at 0, the last accessible index will be 2. If we try and access index 3, we will get an error.
myArray easily accessible through indices in the memory.

Deleting from an array
Removing from the end of the array
In strictly typed languages, all array indices are filled with 0s or some default value upon initialization - this denotes an empty array. Taking this into consideration, when we want to remove an element from the end of an array, we set its value to either 0, or null. It is not being "deleted" per se but rather overwritten by a value that denotes an empty index. The following pseudocode demonstrates the concept using myArray = [4, 5, 6] as an example.

fn removeEnd(myArray, length):
    if length > 0:
        myArray[length - 1] = 0
6 is deleted/overwritten by either 0 or -1 to denote that it does not exist anymore.

Removing at the ith index
Using the same instance of myArray from the previous example, let’s say that instead of deleting at the end, we wanted to delete an element at a random index. Would we be able to perform this in O(1)O(1)? We could just replace it with a zero and call it a day. However, what if the index we wanted to delete at was 00?. If replaced with a 00, we would have an empty first index, which does not make sense.

In the worst case, the random index might be the 00-th index, in which case, upon deletion, all the elements from index 11 all the way till n - 1n−1 will shift one position to the left, where nn is the size of the array. This is seen in the pseudocode and visual below.

fn removeMiddle(myArray, i, length):
    for index = i + 1 to length:
        myArray[index - 1] = myArray[index]


In the worst case, n shifts may be required, therefore the above code will be in O(n)O(n).
Insertion
Inserting at the end of the array
Since we can always access the last index of the array, inserting an element to the end of an array is O(1)O(1) time. Below is pseudocode demonstrating the concept.

fn insertEnd(myArray, n, length, capacity):
    if length < capacity:
        myArray[length] = n
Here, length is the number of indices that are non-empty and capacity is the actual size of the array that is declared upon instantiation. This makes sense because we are assigning the length index, which is the current last index, to n, which is the desired value.
Inserting at the ith index
Inserting in the ith index is a little bit more tricky. With the current state of myArray, we have [4, 5, 0] with the last index being empty. If the ith index is the last index, we know it will be O(1)O(1). But what if it is at index 1, or 0? We cannot overwrite because we would lose our current values. What we can do is shift the current values one position to the right before we insert our new value, say, at index 00. Below is the pseudocode and visual demonstrating this.

fn insertMiddle(myArray, i, n, length):
    for index = length - 1 and index > i - 1:
        myArray[index + 1] = myArray[index]
    myArray[i] = n


First we create space, and then we insert into the desired index.

Closing Notes
Operation	Big-O Time	Notes
Access	    O(1)O(1)	
Insertion	O(n)O(n)*	If inserting at the end of the array, O(1)O(1)
Deletion	O(n)O(n)*	If deleting at the end of the array, O(1)O(1)


## Dynamic Arrays

Dynamic Arrays are much more common and useful because of their ability to be resized. In JavaScript and Python, these are the default — they are not strictly typed languages.

The difference between static and dynamic arrays is that we don’t have to specify a size upon initialization.

In different languages, dynamic arrays maybe assigned a default size - Java being 
10
10 and C# being 
4
4. Regardless, these are resized dynamically by the operating system.

Mechanics of dynamic arrays
When inserting into a dynamic array, the operating system finds the next empty space and pushes the element into it. For the sake of an example, let’s take an array of size 
3
3 and push elements into it until we run out of space. The pseudocode and visual below demonstrate this.

 fn pushback(n):
    if length has reached capacity: 
        resize the array by doubling its size
    arr[length] = n
    length++

Since the array is dynamic, adding another element when we run out of capacity is achieved by copying over the values to a new array that is double the original size - this means that the resulting array will be of size 6 and will have new space allocated for it in memory. The following visual and pseudocode demonstrates this.

fn resize(capacity, arr, length):
   // Create new array of double capacity
   capacity = 2 * capacity
   //declare an array newArr with updated capacity
   
   // Copy elements to newArr
   for i = 0 to length:
       newArr[i] = arr[i]
       
   // update the original array
   arr = newArr

This operation will run in amortized
O(1). Amortized time complexity is the average time taken per operation, that once it happens, it won’t happen again for so long that the cost becomes “amortized”. This makes sense because it is not always that the array needs to be resized, in which case we would perform O(n) operations.

Why double the capacity?
Let’s dig a little bit deeper into why we double the size of the initial array when we run out of space. This can be proven mathematically, so let’s go over a high level overview. Don't worry, we will not be using any fancy equations. The visual below shows a resulting array of size 8. Now imagine that we wanted to dynamically fill it up and we started with a size 1 array. We would add 5, double the space to add 6, double that space to add 7 and 8, double that space to add 9,10, 11 and 12

The size of the above array went from 1 -> 2 -> 4 -> 8. And this makes sense because in order to create the resulting array observed in the visual, we had to create 4 spaces, and then insert
4 elements, which is a total of 8 operations. Additionally, we also have to take into consideration the sum of all the operations that occured before the last one since we would not have gotten to the resulting array without these operations.

The pattern here is that the last term (the dominating term) is always less than or equal to the sum of all the terms before it. In this case, 

1+2+4=7, and 

7<8. Add in the 

8 to the 7, we get a total of 

15 operations to create the resulting array of size 8. Generally, the formula is that for any array size 
n, it will take at most 2n operations to create, which would belong to O(n).

Closing Notes
Operation	- Big-O Time	- Notes
Access	- O(1)	
Insertion	- O(1)∗	- O(n) if insertion in the middle since shifting will be required
Deletion - O(1)∗ - O(n) if deletion in the middle since shifting will be required

Other operations in pseudocode


// Remove the last element in the array
fn popback(length):
    if length > 0: 
        length--
    

// Get value at ith index
fn get(i, length): 
    //if the index exists
    if i < length: 
        return arr[i]

// if the index is out of bounds    
    return -1 

// Insert n at ith index
fn insert(i, n): 
    // If index is reachable
    if i < length: 
        arr[i] = n
        return
    // if the index is out of bounds    
    return

// print values of the array
fn print(length): 
    for i = 0 to length: 
        print arr[i]


## Stacks

