const { BST } = require("./trees_1");

// Write a function that accepts the root of a tree as an arg.
// The function should return a 2D array representing the values at each level of the tree.

function level_values(root) {
    let queue = [{ node: root, level: 0 }];

    let levels = [];

    while (queue.length > 0) {
        let { node, level } = queue.shift();

        if (levels[level] === undefined) {
            levels[level] = [ node.val ];
        } else {
            levels[level].push(node.val);
        }

        if (node.left) queue.push({ node: node.left, level: level+1 });
        if (node.right) queue.push({ node: node.right, level: level+1 });
    }

    return levels;
}

const tree = new BST();

tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(17);
tree.insert(16);

console.log(level_values(tree.root));