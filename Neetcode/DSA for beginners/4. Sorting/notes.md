# Sorting

## Insertion Sort

Insertion sort is one sorting algorithm used to sort data in different data structures. It is one of the simplest sorting algorithms that works best when the data size is small (we will discuss why this is the case soon).

[2,3,4,1,6] -> [1,2,3,6]

think of the algo in subproblems

Solve this prob iteratively using loops

start at second element because the first subarray is also ready sorted (index 0)

Compare the current value to the previous value in the array

if it is larger then stay there and if the value is smaller, it should swap, and then move to the next value

compare to the left neighbor and shift if the value is higher 

stable algo

worst case O(n^2)
best case O(n)


## Merge Sort

one of the most common osrting algos it is really efficient

take the input array and split it into two equals haves and then split those into halfes and keep going until 1 element left(base case)

Naturually leads you to recursion

it is two branch recursion

Divide & conquer technqiue 

stable algo

Big-O time = O(nlogn)


## Quick Sort

Very common sorting algo and common to merge sort

pick a random value (right most value = pivot value)

Iterate every value before the pivot value and compare that value to the pivot value and every value less than or equal to the pivot will be in the left partition of the array

every value greater than the pivot goes to the left and every value greater than the pivt goes to the right

no extra memeoery to do the particion

put the pivot where the pointer ended




## Quick Sort

