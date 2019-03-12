class Node {
  constructor(val) {
    this.val = val;
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

  search(target, root = this.root) {
    if (root === null) return null;

    if (target < root.val) {
      return this.search(target, root.left);
    } else if (target > root.val) {
      return this.search(target, root.right);
    }

    return root;
  }

  // runtime:
  //    O(n)
  dfPrint() {
    let stack = [this.root];

    while (stack.length > 0) {
      let node = stack.pop();
      console.log(node.val);
      if (node.right !== null) stack.push(node.right);
      if (node.left !== null) stack.push(node.left);
    }
  }

  // runtime:
  //    O(n)
  bfPrint() {
    let queue = [this.root];

    while (queue.length > 0) {
      let node = queue.shift();
      console.log(node.val);
      if (node.left !== null) queue.push(node.left);
      if (node.right !== null) queue.push(node.right);
    }
  }
}

// const tree = new BST();
// tree.insert(10);
// tree.insert(5);
// tree.insert(15);
// tree.insert(3);
// tree.insert(7);
// tree.insert(13);
// tree.insert(17);
// tree.insert(11);


// tree.dfPrint();
// tree.bfPrint();
// tree.inOrderPrint();

// console.log(tree.search(11)); // => true
// console.log(tree.search(13)); // => true
// console.log(tree.search(9)); // => false

// WORST CASE B-SEARCH ON BST
//      n is the number of nodes
//  runtime: O(n)
//          when "tree" is really linked list and the val is not found
// BEST CASE
//  runtime: O(logn)
//          when "tree" is balanced


// console.log(tree.height());
// console.log(tree.dfPrint());
// console.log(tree.bfPrint());
// console.log(tree.search(10));



module.exports = { BST };

