const { BST, Node } = require("./trees_1");

const tree = new BST();

tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(17);
tree.insert(16);


// inOrder, preOrder, and postOrder are all depth first traversals
function inOrderPrint(root) {
    if (!root) return;

    inOrderPrint(root.left);
    console.log(root.val);
    inOrderPrint(root.right);
}

function preOrderPrint(root) {
    if (!root) return;

    console.log(root.val);
    preOrderPrint(root.left);
    preOrderPrint(root.right);
}

function postOrderPrint(root) {
    if (!root) return;

    postOrderPrint(root.left);
    postOrderPrint(root.right);
    console.log(root.val);
}

function depthFirstRecur(root) {
    if (!root) return;

    console.log(root.val);
    depthFirstRecur(root.left);
    depthFirstRecur(root.right);
}

function depthFirstIter(root) {
    let stack = [ root ];

    while (stack.length > 0) {
        let node = stack.pop();
        console.log(node.val);

        if (node.right) stack.push(node.right)
        if (node.left) stack.push(node.left);
    }
}

function breadthFirstIter(root) {
    let queue = [root];

    while (queue.length > 0) {
        let node = queue.shift();
        console.log(node.val);

        if (node.left) queue.push(node.left);
        if (node.right) queue.push(node.right)
    }
}


breadthFirstIter(tree.root)