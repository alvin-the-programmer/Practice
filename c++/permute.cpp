#include <algorithm>
#include <iostream>

using namespace std;


void permute(string perm, string orig) {
	string noDups = orig;
	sort(noDups.begin(), noDups.end());
	noDups.erase(std::unique(noDups.begin(), noDups.end()), noDups.end());
	if(orig.empty()) {
		cout << perm << endl;
	}
	for(int i = 0; i < noDups.length(); i++) {
		string pStr = perm;
		string str = orig;
		pStr += noDups[i];
		str.erase(str.find(noDups[i]), 1);
		permute(pStr, str);
	}
}

void permute(string orig) {
	permute("", orig);
}

int main() {
	cout << "string permutations" << endl;
	permute("abca");
	return 0;
}