// March 5, 2019
class Node {
    constructor(val) {
        this.val = val
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    insert(val, root = this.root) {
        // if the tree is empty, then set the abs root to the val
        if (this.root === null) {
            this.root = new Node(val);
            return;
        }

        // if the val is less, go left
        // otherwise go right
        if (val < root.val) {
            if (root.left === null) {
                // if the left tree is empty, then add it here
                root.left = new Node(val);
            } else {
                // otherwise its nonempty, so travel to the left subtree and insert there
                this.insert(val, root.left);
            }
        } else {
            if (root.right === null) {
                root.right = new Node(val);
            } else {
                this.insert(val, root.right);
            }
        }
    }

    inOrderPrint(root = this.root) {
        if (root === null) return;

        this.inOrderPrint(root.left);
        console.log(root.val);
        this.inOrderPrint(root.right);
    }

    height(root = this.root) {
        if (root === null) return -1;
        let leftH = this.height(root.left);
        let rightH = this.height(root.right);
        return Math.max(leftH, rightH) + 1;
    }
}

const tree = new BST();
tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(13);
tree.insert(17);
tree.insert(11);

console.log(tree.height());



// tree.insert(10);
// tree.insert(5);
// tree.insert(15);
// tree.insert(3);
// tree.insert(7);
// tree.insert(17);
// tree.insert(17);
// tree.insert(5);

// tree.inOrderPrint();
// console.log(tree.root);

// Balanced Tree
// - given the root of a tree
//  - the left subtree and right subtree MUST
//        differ in height by at most 1
//  - AND the left subtree is balanced
//  - AND the right subtree is balanced

// BST
// - given the root of a tree
//  - all vals in the left subtree are <
//  - all vals in the right subtree are >=
// - AND the left subtree is a BST
// - AND the right subtree is a BST
// - an empty tree is a BST



// Empty tree has height of -1
// tree with only one node, has height of 0
//

// Why are balanced trees good?
//  - the height of a balanced tree is small
//  - binary search in the worst case will travel the 
//      full height of the tree
//  - binary search will take O(h), where h = height
//  - a balanced tree has height of log(n), where n = # nodes