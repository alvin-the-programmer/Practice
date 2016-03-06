#include <iostream>
#include <vector>

using namespace std;

bool magicIndex(int index, vector<int> a) {
	cout << "magicIndex(" << index << ")" <<endl;
	if(index >= a.size()) {
		cout << "MAGIC INDEX NOT FOUND." << endl;
		return false;
	}
	else if(a[index] == index) {
		cout << "MAGIC INDEX FOUND: " << index << endl;
		return true;
	}
	else if (a[index] > index) {
		magicIndex(a[index], a);
	}
	else {
		magicIndex(index + 1, a);
	}
}

int main() {
	cout << "magic index" << endl;
	vector<int> sortedArr = {-12,-5,5,5,5,5,10,12,16};
	magicIndex(0, sortedArr);

	return 0;
}