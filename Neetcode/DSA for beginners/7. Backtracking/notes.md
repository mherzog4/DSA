# backtracking

## Tree maze

backtracking algo is essentially based on DFS algo

the idea is similar to a maze and reach a dead end and backtrack and try another route

Brute force approach - going through every single possibilty

You have to go through every possibility with back tracking

Questions: Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes.




```python
def canReachLeaf(root):
    if not root or root.val == 0:
        return false

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    path.pop()
    return False
```

