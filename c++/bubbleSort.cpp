#include <iostream>
#include <vector>


using namespace std;

void printVec(vector<int> arr) {
	for(int i = 0; i < arr.size(); i++ ) {
		cout << arr[i] << " ";
	}
	cout<< endl;
}

void bubbleSort(vector<int> arr) {
	bool changed = true;
	while(changed) {
		changed = false;
		for(int j = 0; j < arr.size() - 1; j++) {
			if(arr[j] > arr[j + 1]) {
				int temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
				changed = true;
			}
		}
	}
	printVec(arr);
}

int main() {
	cout << "bubble sort" << endl;
	vector<int> arr = {6,2,4,3,7,3,12,19,-3,2,1,100,99,20,19};

	bubbleSort(arr);
	return 0;
}