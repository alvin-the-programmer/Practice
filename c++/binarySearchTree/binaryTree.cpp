#include <iostream>
#include <vector> 
#include <algorithm>  
#include <stdlib.h> 

#include "binaryTree.h"

using namespace std;

void ins(Node* &node, int data) {
	if(node == NULL) {
		node = new Node;
		node->data = data;
	}
	else if(data < node->data) {
		ins(node->left, data);
	}
	else if(data >= node->data) {
		ins(node->right, data);
	}
}

void BinaryTree::insert(int data) {
	ins(root, data);
}

void pri(Node* node) {
	if(node != NULL) {
		pri(node->left);
		cout << node->data << " ";
		pri(node->right);
	}
}

void BinaryTree::print(void) {
	pri(root);
	cout << endl;
}

int height(Node* node, int h) {
	if(node == NULL) {
		return h;
	}
	else {
		int left = height(node->left, h + 1);
		int right = height(node->right, h + 1);
		if(left == -1 || right == -1) {
			return -1;	
		}
		else if(abs(left - right) > 1) {
			return -1;
		}
		else {
			return max(left, right);
		}
	}
}

bool BinaryTree::isBalanced(void) {
	if (height(root, 0) == -1) {
		return false;
	}
	else {
		return true;
	}
}
