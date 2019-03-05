# Searching and Balanced BSTs

Let's explore the main application of a Binary Search Tree. Since a BST is a sorted data structure, this allows us to conduct the Binary Search algorithm. This algorithm will be similar to the same Binary Search strategy we used on sorted arrays!

### Implementing Binary Search on a BST

Our goal is to implement a `#search` method on our previous `BST` class that will solve the problem:

```
Given a binary search tree and a target value, return a boolean indicating whether or not the target is
contained in the tree.
```

In other words, our `BST#search` should satisfy the following behavior:

```javascript
let tree = new BST();
tree.insert(10);
tree.insert(5);
tree.insert(16);
tree.insert(1);
tree.insert(7);
tree.insert(16);

tree.search(7);     // => true
tree.search(16);    // => true
tree.search(14);    // => false
```

As with many tree problems, this problem lends itself nicely to recursion! Like always, our base case should capture the scenario where the input tree is trivial and we know the answer to the problem without further calculation. If the given tree is empty, then we can be certain that the target is not found in the tree. The logic of our `BST#search` method will be much the same compared to our `binarySearch` function for sorted arrays. Try to interpret the code below and scroll further to the annotated version when you need clarification

```javascript
// assuming our BST class from the previous section
class BST {
    // ...

    search(val, root=this.root) {
        if (!root) return false;

        if (val < root.val) {
            return this.search(val, root.left);
        } else if (val > root.val){
            return this.search(val, root.right);
        } else {
            return true;
        }
    }
}
```

```javascript
// assuming our BST class from the previous section
class BST {
    // ...

    // commented
    search(val, root=this.root) {
        // if the tree is empty, then the target val is not in the tree, so return false
        if (!root) return false;

        // otherwise the tree is not empty, so...
        if (val < root.val) {
            // if the target is less than the root,
            //  then search the left subtree
            return this.search(val, root.left);
        } else if (val > root.val){
            // if the target is greater than the root,
            //  then search the right subtree
            return this.search(val, root.right);
        } else {
            // otherwise, the target must be equal to the root
            // so return true since we found it!
            return true;
        }
    }
}
```

### Height Balance

Before we analyze the time complexity of `BST#search`, we'll first need to learn about height balance. Recalling what we touched on briefly in our chat on binary trees, **height** is defined as the number of edges between the root and farthest leaf in a tree. Note that height is dictated by the **farthest** leaf (think worst case): 

![height](https://s3-us-west-1.amazonaws.com/appacademy-open-assets/data_structures_algorithms/binary_search_trees/images/height.png)

Following this definition, a tree consisting of a single node has height 0. We consider then an empty tree as having height -1. Height is relevant because not all BSTs are created equal! That is, some BSTs have "good / small" heights, others have "bad / large" heights. Take a look at these two BSTs containing identical values, but very different heights:

![balanced_unbalanced](https://s3-us-west-1.amazonaws.com/appacademy-open-assets/data_structures_algorithms/binary_search_trees/images/balanced_unbalanced.png)

`Tree 1` is preferred over `Tree 2`, because `Tree 1` is **balanced**. Balanced Binary Treess will be the most efficient to perform operations on.

For a binary tree to be **balanced**:

+ the left and right subtrees must differ in height by at most 1
+ AND the left subtree is balanced
+ AND the right subtree is balanced

Notice that **balanced** has a recursive definition. Like you probably guessed, the empty tree is considered balanced. This will be the base case of our definition.

### Only the Best Trees Have Logs

A balanced binary tree is incredible to have because it's height is guaranteed to be **O(log<sub>2</sub>(n))**, where n is the number of nodes in the tree. Let's take a look at a few examples:

![log_heights](https://s3-us-west-1.amazonaws.com/appacademy-open-assets/data_structures_algorithms/binary_search_trees/images/log_heights.png)

To make the approximations above, we rounded the result of each log down to the nearest integer. If you are not convinced of how powerful this is, this means that a balanced tree of 1000 nodes will have a height of just 10.

### Time Complexity Analysis of Binary Search for BSTs

Worst case for the algorithm occurs when the target value is not present in the tree. This means that we must traverse a path from root to a leaf, so we must travel the full **height** of the tree in the worst case. However, like we discussed, the height of a tree can vary wildly. We can have a tree with minimal height (a balanced tree like `Tree 1`), or we can have a tree with maximal height (a linked list like `Tree 2`).

+ **O(log(n))** time for a balanced tree:
+ **O(n)** time for unbalanced tree:

### Space Complexity Analysis of Binary Search for BSTs

No additional space is needed for the algorithm, so we have constant **O(1)** space. 

To play devil's advocate, what if we count the recursive stack calls as contributing to the space complexity? Some coding challenges in your job hunt may pose this. If that is the case then our recursive implementation above will use:

+ **O(log(n))** space for a balanced tree
+ **O(n)** space for unbalanced tree

To truly get constant space out of Binary Search, we're going to have to avoid recursion. Can you think of how we can write the algorithm iteratively? We'll save this for the upcoming project :).
