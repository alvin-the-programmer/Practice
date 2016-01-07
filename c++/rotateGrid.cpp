#include <iostream>

using namespace std;

const int NUM_ROWS = 5;
const int NUM_COLS = 5;

void printGrid(int grid[NUM_ROWS][NUM_COLS]) {
	for(int row = 0; row < NUM_ROWS; row++) {
		for(int col = 0; col < NUM_COLS; col++) {
			cout << " " << grid[row][col] << " ";
		}
		cout << endl;
	} 
}

void rotateGrid(int grid[NUM_ROWS][NUM_COLS]) {
	printGrid(grid);
	int rotatedGrid[NUM_ROWS][NUM_COLS];
	for(int row = 0; row < NUM_ROWS; row++) {
		for(int col = 0; col < NUM_COLS; col++) {
			rotatedGrid[col][NUM_ROWS - 1 - row] = grid[row][col];
		}
		cout << endl;
	} 
	printGrid(rotatedGrid);
}

int main() {
	cout << "Rotate Grid 90 degrees" << endl;
	int grid[NUM_ROWS][NUM_COLS] = {{1,2,3,4,5},
									{6,7,8,9,10},
									{11,12,13,14,15},
									{16,17,18,19,20},
									{21,22,23,24,25}};
	rotateGrid(grid);
	return 0;
}