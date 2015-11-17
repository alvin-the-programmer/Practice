#include <iostream>
#include "tripleStack.h"

using namespace std;

int main () {
	cout << "Triple Stack in Array." << endl;
	TripleStack stack;
	stack.print();
	stack.pushA(10);
	stack.pushB(20);
	stack.pushC(30);
	stack.pushA(11);
	stack.pushB(21);
	stack.pushC(31);
	stack.print();
	stack.popA();
	stack.popB();
	stack.popC();
	stack.pushA(12);
	stack.pushB(22);
	stack.pushC(32);
	stack.print();
	return 0;
}