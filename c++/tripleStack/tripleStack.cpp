#include <iostream>
#include "tripleStack.h"

using namespace std;

void TripleStack::print() {
	for(int i = 0; i < 20; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}

void TripleStack::pushA(int item) {
	*a = item;
	a += 3;
}

int TripleStack::popA() {
	a -= 3;
	return *a;
}

void TripleStack::pushB(int item) {
	*b = item;
	b += 3;
}

int TripleStack::popB() {
	b -= 3;
	return *b;
}

void TripleStack::pushC(int item) {
	*c = item;
	c += 3;
}

int TripleStack::popC() {
	c -= 3;
	return *c;
}