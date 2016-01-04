#include <iostream>

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

bool rowIsClear(int row, bool board[NUM_ROWS][NUM_COLS]) {
	for(int col = 0; col < NUM_COLS; col++) {
		if(board[row][col]) {
			return false;
		}
	}
	return true;
}

bool colIsClear(int col, bool board[NUM_ROWS][NUM_COLS]) {
	for(int row = 0; row < NUM_ROWS; row++) {
		if(board[row][col]) {
			return false;
		}
	}
	return true;
}

bool diagIsClear(int row, int col, bool board[NUM_ROWS][NUM_COLS]) {
	for (int i = 0; i < NUM_ROWS; i++) {
		if(row + i < NUM_ROWS && col + i < NUM_COLS) {
			if(board[row + i][col + i]) {
				return false;
			}
		}
		if(row + i < NUM_ROWS && col - i < NUM_COLS && col - i > -1) {
			if(board[row + i][col - i]) {
				return false;
			}
		}
		if(row - i < NUM_ROWS && row - i > -1 && col + i < NUM_COLS) {
			if(board[row - i][col + i]) {
				return false;
			}
		}
		if(row - i < NUM_ROWS && row - i > -1 && col - i < NUM_COLS && col - i > -1) {
			if(board[row - i][col - i]) {
				return false;
			}
		}
	}
	return true;
}

bool isClear(int row, int col, bool board[NUM_ROWS][NUM_COLS]) {
	if(!rowIsClear(row, board)) {
		return false;
	}
	if(!colIsClear(col, board)) {
		return false;
	}
	if(!diagIsClear(row, col, board)) {
		return false;
	}
	return true;
}

void eightQueens(int numQueens, bool board[NUM_ROWS][NUM_COLS]) {
	if(numQueens == 8) {
		count++;
		printBoard(board);
		cout << endl;
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
	cout << "Eight Queens 8x8" << endl;
	eightQueens(0, myBoard);
	cout << count << endl;

	return 0;
}