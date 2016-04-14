#include "pos.h"
#include "paddle.h"

#include <iostream>

using namespace std;

int main() {
	cout << "hello pong." << endl;
	Paddle p(2);
	cout << p.getHeight() << endl;
	return 0;	
}
