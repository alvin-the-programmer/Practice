#include <iostream>

#include "binaryTree.h"

using namespace std;

int main() {
	cout << "Tree Depth Linked List." << endl;
	BinaryTree tree;
	tree.insert(5);
	tree.insert(6);
	tree.insert(7);
	tree.insert(4);
	tree.print();
	cout << tree.isBalanced() << endl;
	return 0;
}