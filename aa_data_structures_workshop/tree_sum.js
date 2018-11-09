const { BST } = require("./trees_1");

// Write a function that accepts the root of a tree as an arg.
// The function should return the total sum of all node values in the tree.

function treeSum(root) {
    if (!root) return 0;

    let leftSum = treeSum(root.left);
    let rightSum = treeSum(root.right);

    return leftSum + root.val + rightSum
}

const tree = new BST();

tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(17);
tree.insert(16);

console.log(treeSum(tree.root));