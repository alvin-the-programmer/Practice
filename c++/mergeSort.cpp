#include <iostream>
#include <vector>

using namespace std;

void printVec(vector<int> A) {
	for(int i = 0; i < A.size(); i++) {
		cout << A[i] << " ";
	}
	cout << endl;
}

vector<int> merge(vector<int> left, vector<int> right) {
	vector<int> result;
	int i = 0;
	int j = 0;
	while(i < left.size() || j < right.size()) {
		if(i == left.size()) {
			result.push_back(right[j]);
			j++;
		}
		else if(j == right.size()) {
			result.push_back(left[i]);
			i++;
		}
		else if(left[i] < right[j]) {
			result.push_back(left[i]);
			i++;
		}
		else if(left[i] >= right[j]) {
			result.push_back(right[j]);
			j++;
		}
	}
	return result;
}

vector<int> mergeSort(vector<int> A) {
	if(A.size() <= 1) {
		return A;
	}
	int mid = A.size() / 2;
	vector<int> left;
	vector<int> right;	
	for(int i = 0; i < A.size(); i++) {
		if(i < mid) {
			left.push_back(A[i]);
		}
		else {
			right.push_back(A[i]);
		}
	}
	left = mergeSort(left);
	right = mergeSort(right);
	return merge(left, right);
}

int main() {
	cout << "merge sort" << endl;
	vector<int> v = {6,2,4,3,7,3,12,19,-3,2,1,100,0,-25,99,20,19};
    printVec(mergeSort(v));
	return 0;
}