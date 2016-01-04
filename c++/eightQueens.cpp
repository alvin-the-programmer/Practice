#include <iostream>
#include <cmath>

using namespace std;

const int NUM_ROWS = 8;
const int NUM_COLS = 8;

int count = 0;

bool myBoard[NUM_ROWS][NUM_COLS];

void printBoard(bool board[NUM_ROWS][NUM_COLS]) {
	for(int row = 0; row < NUM_ROWS; row++) {
		for(int col = 0; col < NUM_COLS; col++) {
			cout << " " << board[row][col] << " ";
		}
		cout << endl;
	} 
}

bool isClear(int row, int col, bool board[NUM_ROWS][NUM_COLS]) {
	for(int r = 0; r < NUM_ROWS; r++) {
		for(int c = 0; c < NUM_COLS; c++) {
			if(r == row && board[r][c]) {
				return false;
			}
			if(c == col && board[r][c]) {
				return false;
			}
			if(abs(row - r) == abs(col - c) && board[r][c]) {
				return false;
			}
		}
	}
	return true;
}

void eightQueens(int numQueens, bool board[NUM_ROWS][NUM_COLS]) {
	if(numQueens == 8) {
		count++;
		printBoard(board);
		cout << endl;
		return;
	}
	else {
		for(int row = numQueens; row < NUM_ROWS; row++) {
			for(int col = 0; col < NUM_COLS; col++) {
				if(isClear(row, col, board)) {
					bool newBoard[NUM_ROWS][NUM_COLS];
					for(int i = 0; i < NUM_ROWS; i++) {
						for (int j = 0; j < NUM_COLS; j++) {
							newBoard[i][j] = board[i][j];
						}
					}
					newBoard[row][col] = true;
					eightQueens(numQueens + 1, newBoard);
				}
			}
		} 
	}
}

int main() {
	eightQueens(0, myBoard);
	cout << "Eight Queens 8x8." << endl;
	cout << "Number of Possible Configurations: " << count << endl;

	return 0;
}