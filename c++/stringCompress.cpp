#include <iostream>

using namespace std;

const string shorter = "abbcccddddcccbbabaa";
const string longer = "abcdeef";


string stringCompress(string s) {
	string compr = "";
	int i = 0;
	char c = 0;
	for(int i = 0; i < s.size();) {
		c = s[i];
		int counter= 0;
		for(i; i < s.size() && s[i] == c; i++) {
			counter++;
		}
		compr += c + to_string(counter);
	}
	if(compr.size() < s.size()) {
		return compr;
	}
	else {
		return s;
	}
}

int main() {
	cout << "string compress" << endl;
	cout << shorter << endl;
	cout << stringCompress(shorter) << endl;
	cout << longer << endl;
	cout << stringCompress(longer) << endl;

	return 0;
}