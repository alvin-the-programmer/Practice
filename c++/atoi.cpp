#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int ctoi(char c) {
	if(c == '0') return 0;
	if(c == '1') return 1;
	if(c == '2') return 2;
	if(c == '3') return 3;
	if(c == '4') return 4;
	if(c == '5') return 5;
	if(c == '6') return 6;
	if(c == '7') return 7;
	if(c == '8') return 8;
	if(c == '9') return 9;
}

int myatoi(string s) {
	int sum = 0;
	for(int i = s.length() - 1; i >= 0; i--) {
		int ex = s.length() - 1 - i;
		sum += ctoi(s[i]) * pow(10,ex);
	}
	return sum;
}

int main() {
	cout << myatoi("1776") << endl;
	return 0;
}