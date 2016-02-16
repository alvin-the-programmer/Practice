#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> arr) {
	for(int i = 0; i < arr.size(); i++ ) {
		cout << arr[i] << " ";
	}
	cout<< endl;
}

vector<int> quickSort(vector<int> A) {
	if(A.size() <= 1) {
		return A;
	}
	int pivot = A.back();
	A.pop_back();
	vector<int> left;
	vector<int> right;
	for(int i = 0; i < A.size(); i ++) {
		if(A[i] < pivot) {
			left.push_back(A[i]);
		}
		else if(A[i] >= pivot) {
			right.push_back(A[i]);
		}
	}
	left = quickSort(left);
	right = quickSort(right);
	left.push_back(pivot);
	left.insert(left.end(), right.begin(), right.end());
	return left;
}

int main() {
	cout << "quick sort" << endl;
	vector<int> v = {10,12,64,1,-12,3,5,9,7,5,3,0,100,10,99,3};
	printVec(v);
	printVec(quickSort(v));

	return 0;
}