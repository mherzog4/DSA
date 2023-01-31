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

```python
from collections import deque

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

print(bfs(grid))
```

this pattern is common  with the shortest path algo




## Adjacency List

theres are more simpler to run an algo on than a matrix

in coding interviews its more common to use a hashmap to represent an adjacency list - because the value/id of each id when it is unique and the value is a list and the list represent the neighbors

src is the first in the pair

dst is the second in the pair

want to make sure every node is added to the adjancency list

for the adjacency list of the src (a) append the neighbors(b)

A points to B

B has already been added to adjacnency list but C has not

you can run BFS and DFS on this

Graphs come up a ton in coding interviews

what if the edges have a different lengths




```python
from collections import deque

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Or use a HashMap
adjList = { "A": [], "B": [] }

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)


# Count paths (backtracking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count

# Shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length

```