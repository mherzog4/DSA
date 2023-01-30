# Graphs

really common for coding interviews & pretty challenging

## intro to graphs

Linked lists are a subset of graphs

and trees are a subset of grapsh

 a graph is made up of nodes and pointers that connect them together

 A node is the same thing as a verticiy

 when a node is connected to another node it is called edges

 When it comes to geneeric graphs there are no restrictions with nodes and edges 

 Edges <= verticy^2

A directed graph means that every pointer/edge has a one way flow of direction

an undirected graph means you can go in either direction

3 way common ways to define a graph

1. matrix
2. adjacency matrix
3. adjacency list

1. A matrix is a two dimensional array

``` python
grid = 
[[0,0,0,0],
[1,1,0,0],
[0,0,0,1],
[0,1,0,0]]

```
0 - free
1 - blocked

4 rows & 4 columns

use 'r' and 'c' to define the rows and columns to implement the coordinates

everything is indexed by 0

2. adjacnecny matrix

less common in coding interviews

ajdMatrix[v1][v2] = 1
- an edge case exists from v1 to v2

adjMatrix[v2][v1] = 1
- an edge exists from v2 to v1

the space complexity is O(v^2) where v is the amount of verticies

3. Adjacency list

the most common way to represent graphs in coding interviews

``` python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
```
## Matrix DFS

very common algo because it is frequently applied to graphs

it is pretty much backtracking - both recursive and similiar

``` python
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

```

## Matrix BFS

## Adjacency List

