# trees

## Binary trees

similar to linked lists where you have nodes and the nodes need poitners to connect them together

those nodes have two pointers

similar to doubly linked list node and drown the pointers down

The nodes has a relationship between each other (child relationship)

The node above the child node is called the parent node and the parent node can have children nodes

Nodes that dont have any children are called leaf nodes

Binary trees always guaranteed to have leaf nodes

the top node is called the root node

binary trees cant have cycles

the height property is the height of the tree and you start at the top node and go down to the lowest descendant node (like rows going down)

ancestor nodes is any node that goes back up the chain past the parent node

Depth is the oposite concept of height

measures the path from a node to the root node (like rows going up from starting node)



## Binary search tree

Like binary trees but they have a sorting property to them

allows us to use the sorting similar to a sorting array

for every node in tree the guarantee of BST is that every node in the left sub tree has to be less than the root value and every value in the node subtree has to be greater than the root value

BST do not contain duplicates

balance binary search tree is O(logn)

the time complexity of search is big O(h) where h is the height of the tree

Why do we have binary search trees if we have sorted arrays?

Because the down side of sorted arrays if you want to add or remove values of array and keep sorted properties of the value you have to shift the value of the array

BST insertion and deletion can be O(logN)

## BST Insert and remove

### inserting

inserting traverse the height of the tree

it is usually easier to add nodes as leaf nodes to the tree

the time complexity is the same as searching

O(logn) if you have a balanced tree

### Removing

Finding the minimun (findmin) of the tree goes to the left of the nodes and go down to the left

``` python
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr
```

two case when removing

- case 1: 0 or 1 child
- case 2: 2 children

case two is more difficult

case 1:

similiar to searching but don't have to look through every property because it is sorted

after removing node return null to the parent and the parent node assigns the left pointer to null so the node is not connected to the tree

case 2:

check if the right and left pointers are null

the easiest thing to do is to replace the parent node with one of its children

recursively call the function on the right subtree and once that removal is finished 

``` python
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
        return root

```
O(logn) - have to traverse the tree twice

## Depth first search - BST Traversal

we want to go left to right

before we pop back up to the parent, traverse the sub-tree of the node right after you process the node itself

inorder traversal example:

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

the time complexity of the above you have to traverse the entire tree and visit each node and that makes it the size of the tree O(n) - the same as traversing an array

pre-order traversal example:
``` python
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
```

post-order traversal example:
``` python
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```
O(n) time complexity

all three of the above recursive functions are DFS

As name suggests you go depth first - go as far deep as you can first

get to the bottom of the tree first and then go back up

the opposite of DFS is BFS

BFS goes layer by layer

## Breadth-first search

Instead of going for depth you go wide and go layer by layer

go left to right in trees

print the root node and go to next left node

this algo doesnt suite recursion well - do this algo iteratively

after processes a node print the children of the node

implement a queue - first in first out

``` python
from collections import deque

def bfs(root):
    queue = dequue()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range (lef(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
```

## BST Sets and Maps

sets and maps are common with binary search trees

a set is similiar to an array

can insert and remove values in logn time

Maps

lke a phonebook A-Z and every name is mapped to other contact info (phone #)

Key Value pairing

the data structure is sorted by the key

BST is the underlying data structure of sets and maps

Python doesnt have native tree maps

