#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class setOfStacks {
	private:
		vector<stack<int>*> stacks;
	public:
		setOfStacks(void);
		void push(int item);
		int pop(void);
		int popStack(int num);
};

setOfStacks::setOfStacks(void) {
	cout << "constructing" << endl;
	cout << "new stack" << endl;
	stack<int>* s = new stack<int>;
	stacks.push_back(s);
}

void setOfStacks::push(int item) {
	stack<int>* s = stacks.back();
	if(s->size() < 3) {
		s->push(item);
	}
	else {
		cout << "new stack" << endl;
		stacks.push_back(new stack<int>);
		s = stacks.back();
		s->push(item);
	}
	cout << "push " << item << endl;
}

int setOfStacks::pop(void) {
	stack<int>* s = stacks.back();
	int item = s->top();
	s->pop();
	if(s->empty()) {
		cout << "deleting stack" << endl;
		delete s;
		stacks.pop_back();
	}
	cout << "pop " << item << endl;
	return item;
}

int setOfStacks::popStack(int num) {
	stack<int>* s = stacks[num];
	int item = s->top();
	s->pop();	
	if(s->empty()) {
		delete s;
		stacks.erase(stacks.begin() + num);
	}
	cout << "targeted pop " << item << endl;
	return item;
}

int main() {
	setOfStacks myStacks;
	myStacks.push(1);
	myStacks.push(2);
	myStacks.push(3);
	myStacks.push(4);
	myStacks.push(5);
	myStacks.push(6);
	myStacks.push(7);
	myStacks.push(8);
	myStacks.push(9);
	myStacks.popStack(1);
	myStacks.popStack(1);
	myStacks.popStack(1);
	myStacks.pop();
	myStacks.pop();
	myStacks.pop();
	myStacks.pop();
	myStacks.pop();
	myStacks.pop();
	return 0;
}