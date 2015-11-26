#include <iostream>
#include <stack>

using namespace std;


class SortStack {
	private:
		stack<int> s;
	public:
		void push(int item);
		int pop(void);
};

void SortStack::push(int item) {
	if(!s.empty()) {
		stack<int> temp;
		while(s.top() < item) {
			temp.push(s.top());
			s.pop();
			if (s.empty()) {
				break;
			}
		}
		s.push(item);
		while(!temp.empty()) {
			s.push(temp.top());
			temp.pop();
		}
	}
	else {
		s.push(item);
	}
}

int SortStack::pop(void) {
	int item = s.top();
	cout << "pop " << item << endl;
	s.pop();
	return item;
}

int main () {
	cout << "hello" << endl;
	SortStack myStack;
	myStack.push(5);
	myStack.push(7);
	myStack.push(4);
	myStack.push(3);
	myStack.push(10);
	myStack.push(9);
	myStack.push(1);
	myStack.push(2);
	myStack.push(6);
	myStack.push(8);
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();
	myStack.pop();


}