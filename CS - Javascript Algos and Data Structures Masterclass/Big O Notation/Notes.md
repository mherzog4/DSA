# Big O Notation

## Into to Big O

How can we determine which implementation of the same function is the best?

The answer is Big O

we can use big O for numeric representation of the code

useful for discussing tade-offs between different approaches

able to identifyi parts of the code that are inefficient

## Timing our code

suppose we want to write a function that calculates the sum of all numbers from 1 up to and including some number n

examples

```javascript
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;)
    }
return total;
}
```

```Javascript
function addUpTo(n) {
    return n * (n + 1)  /2;
}
```

Different machines will record different times - so it is not reliable

The same machine will record different times

for fast algos speed measurements may not be precise enough

## Counting Operations

rather than counting seconds which are variable

lets count the number of simple operations the computer has to perform

```Javascript
function addUpTo(n) {
    return n * (n + 1)  /2;
}
```

3 operations

```Javascript
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;)
    }
return total;
}
```
if n = 5 then we have 5 operations

n additions
n assignments

as n grows there aer more additions and assignmenets since it is a loop

Doesnt have to be specific just look at generalizations

the number of operations grows roughly proportionally with n

with Big O we are focused on general trends and big picture

## Official Intro to Big O

Big O Notation is a way to formalize fuzzy counting

it allows us to talk formally about how the runtime of an algo grows as the inputs grow

we wont care about the details, only the trends

Big O Definition:

We say that an algo is O(f(n)) if the number of simple operations the computer has to do is eventially less than a constant times f(n) as n increases

- f(n) could be linear (f(n) = n)
- f(n) could be quadratic (f(n) = n^2)
- f(n) could be constant (f(n) = 1)
- f(n) could be something entirely different!

when we talk aboout Big O we are talking about the worst case scenario


```Javascript
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;)
    }
return total;
}
```
Number of opertaions is bounded by a multiple of n - so it is O(n)

```Javascript
function addUpTo(n) {
    return n * (n + 1)  /2;
}
```
always 3 operations - so it is O(1)


``` javascript
function printAllPairs(n) {
    for (var i =0; i < n; i++) {
        for (var j = 0; j < n; j++) {
            console.log(i, j);
        }
    }
}
```

a nested loop would be o(n^2)

O(n) operation inside of an O(n) operation


## Simplifying Big O Expressions

Depending on what we count, the number of operations can be as low as 2n or as high as 5n + 2 

But regardless of the exact number, the number of operations grows roughly proportionally with n

If n doubles, the number of operations will also roughly double

When determining the time complexity of an algorithm, there are some helpful rule of thumbs for big O expressions.

These rules of thumb are consequences of the definition of big O notation.

O(2n) = O(n)

O(500) O(1)

O(13n^2) O(n^2)

1. Arithmetic operations are constant
2. Variable assignment is constant
3. Accessing elements in an array (by index) or object (by key) is constant
4. In a loop, the the complexity is the length of the loop times the complexity of whatever happens inside of the loop

## Space Complexity

So far, we've been focusing on time complexity: how can we analyze the runtime of an algorithm as the size of the inputs increases?

We can also use big O notation to analyze space complexity: how much additional memory do we need to allocate in order to run the code in our algorithm?

What about the inputs?

Sometimes you'll hear the term auxiliary space complexity to refer to space required by the algorithm, not including space taken up by the inputs.

Unless otherwise noted, when we talk about space complexity, technically we'll be talking about auxiliary space complexity.

Space Complexity in JS

Rules of Thumb

1. Most primitives (booleans, numbers, undefined, null) are constant space
2. Strings require O(n) space (where n is the string length)
3. Reference types are generally O( n), where n is the length (for arrays) or the number of keys (for objects)

## Logs and Section Recaps

We've encountered some of the most common complexities: O(1), O(n), O(n^2)

Sometimes big O expressions involve more complex mathematical expressions

One that appears more often than you might like is the logarithm!

Wait, what's a log again?

log2(8) = 3 -> 2^3 = 8


log2(value) = exponent -> 2^exponent=value

We'll omit the 2.

log === log2

The logarithm of a number roughly measures the number of times you can divide that number by 2 before you get a value that's less than or equal to one.

8
4
2
1
log(8) = 3 

Logarithmic time complexity is great!

Who Cares?

Certain searching algorithms have logarithmic time complexity.

Efficient sorting algorithms involve logarithms.

Recursion sometimes involves logarithmic space complexity.

## Recap

- To analyze the performance of an algorithm, we use Big O Notation
- Big O Notation can give us a high level understanding of the time or space complexity of an algorithm
- Big O Notation doesn't care about precision, only about general trends (linear? quadratic? constant?)
- The time or space complexity (as measured by Big O) depends only on the algorithm, not the hardware used to run the algorithm
- Big O Notation is everywhere, so get lots of practice!