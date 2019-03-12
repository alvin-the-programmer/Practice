const { BST } = require("./trees_2");

// Write a function that accepts the root of a tree as an arg.
// The function should return the maximum sum of a path through the tree.
// For this problem, a path must begin at the root and end at a leaf.

function maxPathSum(root) {
    if (root === null) return -Infinity;
    let leftSum = maxPathSum(root.left);
    let rightSum = maxPathSum(root.right);
    let best = Math.max(leftSum, rightSum)
    if (best === -Infinity) {
        return root.val;
    } else {
        return root.val + best;
    }
}

const tree = new BST();

// tree.insert(-10);
// tree.insert(-5);
// tree.insert(-15);
// tree.insert(-3);
// tree.insert(-7);
// tree.insert(-17);
// tree.insert(-16);

// tree.insert(-4);
// tree.insert(-5);
// tree.insert(-6);

console.log(maxPathSum(tree.root));