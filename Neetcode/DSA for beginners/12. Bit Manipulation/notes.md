# Bit Manipulation

not that important for coding interviews but is something that comes up

understanding the basics is good

bits and 0's and 1's

XOR occasionally comes up in coding interviews - similar to 'or' but its an exclusive or 'XOR'



``` python

# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1

# Counting Bits
def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1 # same as n // 2
    return count

```
