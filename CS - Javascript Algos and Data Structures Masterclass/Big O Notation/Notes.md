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

## Space Complexity

## Logs and Section Recaps
