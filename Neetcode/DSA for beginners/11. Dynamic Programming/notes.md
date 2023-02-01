# Dynamic Programming

## 1 Dimension DP

the fibonacci is an instance of a 1 dimension dp problem

you can take a recursive problem and convert it to dynamic programming

a technique of optimization is memoization

you can cache after you calculate once, so you don't have to recreate the work

solving technique:

do a recursive solution
add memoization
then dynamic programming

use a hashmap to represent the cache


memoization is aka caching is aka top down Dynamic Programming

bottom up of dynamic programming - start at the bottom of the tree


``` python

# Brute Force
def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)

# Memoization
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]

# Dynamic Programming
def dp(n):
    if n < 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]

```

## 2 dimension DP

Question: Count the number of unique paths from the top left to the bottom right - you are only allowed to move down or to the right

Brute force is a decision tree with two branches

use caching to imporve the time complexity



``` python 
# Brute Force - Time: O(2 ^ (n + m)), Space: O(n + m)
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    
    return (bruteForce(r + 1, c, rows, cols) +  
            bruteForce(r, c + 1, rows, cols))

print(bruteForce(0, 0, 4, 4))

# Memoization - Time and Space: O(n * m)
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1
    
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) +  
        memoization(r, c + 1, rows, cols, cache))
    return cache[r][c]

print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))

# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
def dp(rows, cols):
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]
        prevRow = curRow
    return prevRow[0] 

```