# Recursion

What is recursion?
A process (a function in our case) that calls itself

It's EVERYWHERE!

JSON.parse / JSON.stringify
document.getElementById and DOM traversal algorithms
Object traversal
Very common with more complex algorithms
It's sometimes a cleaner alternative to iteration

## Why use Recursion

How recursive functions work
Invoke the same function with a different input until you reach your base case!

Base Case
The condition when the recursion ends.

This is the most important concept to understand

Two essential parts of a recursive function!

- Base Case
- Different Input





## Our first recursive function

Our first recursive function

function countDown(num){
    if(num <= 0) {
        console.log("All done!");
        return;
    }
    console.log(num);
    num--;
    countDown(num);
}

## Our second recursive function

Our second recursive function
function sumRange(num){
   if(num === 1) return 1; 
   return num + sumRange(num-1);
}
Can you spot the base case?

Do you notice the different input?

What would happen if we didn't return?

The ALL important `return` keyword
function sumRange(num){
   if(num === 1) return 1; 
   return num + sumRange(num-1);
}
Let's break this down step by step!

## Writing factorial iteratively

## Writing Factorial Recursively

## Common Recursion Pitfalls

## Helper Method Recursion

## Pure Recursion

