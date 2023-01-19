# Recursion

## Factorial recursion

also known as N factorial

n! is shorthand for n*(n-1)*(n-2) ... all the way till * 1

5! = 5 * 4 * 3 * 2 * 1 = 120

5! = 5 * 4!

n! = n*(n-1)

recursion is all about sub  problems

code for 5! 

the best way to solve recursion is using a decision tree

1 is the base case because that is where the deicsion tree ends and doesnt use the formula anymore


``` python
int factorial (int n) {
    if(n <=1 {
        return 1;
    })
    return n * factorial(n-1);
}
```

each function is taking up memory because of the variables that are in involed

n functions calls

non-recursive solution

``` python
int res = 1
while n > 1 {
    res = res*n;
    n -= 1;
}
```

## Fibonacci Sequence

Two-branch

fibonacci number: F(n) = F(n-1) + F(n-2)
base case ->      F(0) = 0,F(1) = 1

F(5) -> can be broken up into subproblems

Now its time to break into a decision tree

``` python

int fib(int n) {
    if (n <=1) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}
```
to get the nth fib numbe you have to break it up into 2 sub problems until you reach the base case end

nth fibonacci = n layers

to get the number of inputs in the last level you do 2^n