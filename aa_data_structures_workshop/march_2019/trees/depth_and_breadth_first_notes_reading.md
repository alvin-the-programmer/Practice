# Depth and Breadth First Traversal

Let's add two more tree traversal algorithms to our arsenal. **Depth-First** and **Breadth-First** are two classic traversal strategies that differ in the order nodes are hit. In this reading, our candidate tree will be:

![tree](https://s3-us-west-1.amazonaws.com/appacademy-open-assets/data_structures_algorithms/trees/images/graph_a.png)

Like we are accustomed to, we can represent the tree programmatically with:

```javascript
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

let a = new TreeNode('a');
let b = new TreeNode('b');
let c = new TreeNode('c');
let d = new TreeNode('d');
let e = new TreeNode('e');
let f = new TreeNode('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
```

## Depth-First

To help verbalize Depth-First (DF), we'll be using a few familial terms to describe the relative positions of the nodes. Think of the words you would use if viewing a family tree! Here are some examples:

+ `B` and `C` are siblings
+ `D` and `E` are descendants of `B`
+ `B`, `C`, `D`, `E`, `F` are all descendants of `A` 

A Depth-First traversal will continually travel deeper into a tree before switching branches. This means that, given a node, we must visit all of it's descendants before visiting it's sibling.

Performing DF on our tree will hit the nodes in the order: `A, B, D, E, C, F`

### Depth-First Implementation

To travel the nodes of a tree according to Depth-First behavior, we'll utilize a **stack.** Recall from earlier that a stack is LIFO (Last In, First Out). Our strategy is to use an array as a stack. We'll use `push` to add to the top of our stack and `pop` to remove the top. Below is a complete implementation of `depthFirst`. Try to interpret the code below and scroll further to see the annotated version:

```javascript
function depthFirst(root) {
    let stack = [ root ];
    while (stack.length) {
        let node = stack.pop();
        console.log(node.val);
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
    }
}
```

```javascript
function depthFirst(root) {
    // initialize the stack with the root node
    let stack = [ root ];

    // continue running the algorithm while there are still nodes on the stack
    while (stack.length) {

        // pop the top node from the stack
        let node = stack.pop();

        // we consider a node visited once we pop it,
        // so we should print the node's value now
        console.log(node.val);

        // add the node's left and right children, if they exist
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);

        // IMPORTANT: do not print out the children yet; they must wait their turn to be popped first
    }
}
```

You should watch the video lecture that follows this reading for a visual on how a stack inherently gives us DF order. For now, a key idea to take away is that we only consider a node "visited" once we pop it. We do not consider a node "visited" when we push it.

Because a stack naturally leads to DF order on a tree, we can easily write a recursive version. Why is recursion relevant to DF? Recursion utilizies the call **stack**:

```javascript
function depthFirstRecur(root) {
    if (!root) return;
    console.log(root.val);
    depthFirstRecur(root.left);
    depthFirstRecur(root.right);
}
```

Does this code look familiar? It's identical to the `preOrderPrint` function we wrote previously. That's right, pre-order and depth-first are identical tree node orderings.

You should study both the iterative and recursive implementations as they will both prove valuable to solving problems.

## Breadth-First

This algorithm has nothing to do with bread. The word "breadth" is the same as "width". To help veribalize Breadth-First (BF) we'll need to understand the simple concept of tree **levels**. With the tree at the top of this reading in mind, we can say the following:

+ level 0 contains `A`
+ level 1 contains `B`, `C`
+ level 2 contains `D`, `E`, `F`

A Breadth-First traversal will visit all nodes across a level, before moving to the next level. This means we travel laterally as much as we can before going deeper into the tree.

Perform BF on our tree will hit the nodes in the order: `A, B, C, D, E, F`

### Breadth-First Implementation

While DF uses a stack, BF will use a **queue**. Recall that a queue is FIFO (First In, First Out). The code is very similar to our iterative DF, except we will use an array as a queue. `shift` will remove the front of the queue and `push` will add to the back of the queue. Interpret the implementation below and scroll further to the annotated version when you need more insight:

```javascript
function breadthFirst(root) {
    let queue = [ root ];
    while (queue.length) {
        let node = queue.shift();

        console.log(node.val);

        if (node.left) queue.push(node.left);
        if (node.right) queue.push(node.right);
    }
}
```

```javascript
function breadthFirst(root) {
    // initialize the queue with the root node
    let queue = [ root ];

    // continue running the algorithm while there are still nodes on the queue
    while (queue.length) {
        // remove the front node from the queue
        let node = queue.shift();

        // the node we just removed is now "visited", so print it
        console.log(node.val);

        // add the left and right children to the back of the queue, if they exist
        if (node.left) queue.push(node.left);
        if (node.right) queue.push(node.right);

        // IMPORTANT: do not print out the children yet; they must wait their turn to exit the front of the queue first
    }
}
```

We'll rarely run into a recursive BF implementation (probably never) because recursion uses an underlying call stack, but we really want the opposite of a stack (a queue). 