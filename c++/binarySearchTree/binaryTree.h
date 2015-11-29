#ifndef _BINARY_TREE_H_
#define _BINARY_TREE_H_

struct Node {
	int data;
	Node* left = NULL;
	Node* right = NULL;
};

class BinaryTree {
	private:
		Node* root = NULL;
	public:
		void insert(int data);
		void print(void);
		bool isBalanced(void);

};

#endif