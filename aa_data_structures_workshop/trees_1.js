// Tree Keys to Victory :)
//   * a tree containing 0 nodes is still a tree, although an empty tree
//   * a tree has no cycles
//   * a tree contains many (sub)trees, lending itself to recursion
//
// DEFINITIONS:
//
// Graph  - a structure containing nodes and edges
//        - a node may contain data, an edges connect two nodes
//        - visually we use circles as nodes and arrows as edges
//        - programmatically we use node instances as nodes and references as edges
//
// Tree   - a graph with no cycles
//        - having no cycles means that we can designate a root, the root is the "start" point
//          - if we allow cycles: who is the parent? who is the child? - This is why we don't allow them.
//        - if we have access to the root, then we have access to the full tree,
//          b/c there is a path to every node from the root.
//        - having a single node is a tree
//        - having no nodes is a tree
//        - this means that the definition of a tree is recursive
//
// Binary Tree - a tree where every node has 0, 1, or 2 children
//
// Binary Search Tree - a binary tree where the left subtree contains values less than the root,
//                      the right subtree contains values greater than or eq to root...
//                    - AND the left subtree is a binary search tree...
//                    - AND the right subtree is a binary search tree.
//                    - an empty tree is a binary search tree
//                    - this means that the definition of a BST is recursive
//
// Balanced Binary Tree - binary tree where the heights of the left and right subtrees differ by at most 1.
//                      - AND the left subtree is balanced
//                      - AND the right subtree is balanced
//                      - an empty tree is balanced binary tree
//                      - this means that the definition of balanceness is recursive
//
// WRAPPING UP
//    - Our implementation of a BST doesn't guarantee it to be balanced after any arbitrary insertions.
//
//    - How to delete any node from BST? It's pretty involved:
//      - find the the node
//      - keep swapping that node with it's greater child until it is a leaf (at the bottom of the tree)
//        - swapping with the greater child always guarantees search tree property is not broken
//      - chop off the leaf, by setting it's parent's reference to null
//
//    - Tree Height Interpretations
//      - Alvin consider's an empty binary tree as having height 0,
//        so a tree with a single node has height 1.
//      - Another valid interpretation is that an empty tree is height -1,
//        so a tree with a single node has height 0
//
// HOMEWORK
//    - Reimplement your own BST class with the same methods.
//      - #insert
//        - our insert logic is pretty redundant, can you DRY it up?
//      - #print
//      - #search
//
//    - Then re-reimplement it without recursion.
//      - which one do you prefer recursive or iterative?
//
//    - Implement #delete(val) using the previously mentioned steps
//
//                                                Thanks for Attending! -AZ

class Node  {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null; // an empty tree's root is null.
  }

  // print is an inOrderTraversal which is a type of depthFirstTraversal
  print(root=this.root) {

    // since we are printing a search tree,
    // we know all nodes in the left subtree are less than root,
    // and all nodes in the right subtree are greater than root.
    if (!root) return;

    // so print the left subtree...
    this.print(root.left);
    // then the current root...
    console.log(root.val);
    // and finally the right subtree...
    this.print(root.right);
  }

  search(val, root=this.root) {
    // if the tree is empty,
    // then the val is certainly not going to be found
    if (!root) return false;

    // if the root contains the value, we successfully found the val!
    if (root.val === val) return true;

    // otherwise, the root does not contain the value, so...
    if(val < root.val) { // go left if our target val is less
      return this.search(val, root.left);
    } else {             // go right if our target val is greater or eq
      return this.search(val, root.right);
    }
  }

  insert(val, root=this.root) {
    // if the tree is empty,
    // then simply set this.root to make the initial node
    if (!root) {
      this.root = new Node(val);
      return;
    }

    // otherwise the tree is not empty,
    // so decide which subtree to insert into based on value of current root

    if (val < root.val) { // go to left subtree
      if (root.left) {
        // if the left subtree exists,
        // so we insert into that subtree
        this.insert(val, root.left);
      } else {
        // else the left subtree does not exist,
        // so create the node at that position
        root.left = new Node(val);
      }
    } else {             // go to right subtree
      if (root.right) {
        this.insert(val, root.right);
      } else {
        root.right = new Node(val);
      }
    }
  }
}

let tree = new BST();

tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(17);

tree.print();

console.log(tree.search(7));
console.log(tree.search(1000));
