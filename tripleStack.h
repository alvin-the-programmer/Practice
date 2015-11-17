#ifndef _TRIPLESTACK_H_INCLUDED_
#define _TRIPLESTACK_H_INCLUDED_

class TripleStack {
	private:
		int arr[20];
		int* a = &arr[0];
		int* b = &arr[1];
		int* c = &arr[2];
	public:
		void print();
		void pushA(int item);
		void pushB(int item);
		void pushC(int item);
		int popA();
		int popB();
		int popC();
		
};













#endif