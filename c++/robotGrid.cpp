#include <iostream>
#include <vector>

using namespace std;


void pathFinder(bool maze[9][9], bool (&memo)[9][9], vector<vector<int>> path, int row, int col) {
	if(memo[row][col]) {
		return;
	}
	else {
		memo[row][col] = true;
	}
	if(row == 8 && col == 8) {
		cout << "found path" << endl;
		for(int i = 0; i < path.size(); i++) {
			for(int j = 0; j < 2; j++) {
				cout << path[i][j];
			}
			cout << endl;
		}
		return;
	}
	if(row < 8) {
		if(maze[row + 1][col] == true) {
			vector<int> point = {row + 1, col};
			vector<vector<int>> newPath = path;
			newPath.push_back(point);
			pathFinder(maze, memo, newPath, row + 1, col);
		}
	}
	if(col < 8) {
		if(maze[row][col + 1] == true) {
			vector<int> point = {row, col + 1};
			vector<vector<int>> newPath = path;
			newPath.push_back(point);
			pathFinder(maze, memo, newPath, row, col + 1);
		}
	}
}


int main() {
	cout << "Robot Grid Pathfinder." << endl;

	bool maze[9][9] = {
						{1,1,1,1,1,1,1,1,1},
						{1,1,1,1,1,1,1,1,1},
						{0,1,1,1,0,1,1,1,1},
						{1,1,1,1,1,1,0,0,1},
						{1,1,0,1,1,1,1,0,1},
						{1,1,1,0,1,1,1,0,1},
						{1,1,1,1,1,1,1,0,1},
						{1,1,1,0,1,1,1,0,1},
						{0,1,1,1,1,0,1,0,1}
	};
	bool memo[9][9] = {
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0},
						{0,0,0,0,0,0,0,0,0}
	};
 	vector<vector<int>> path;
 	pathFinder(maze, memo, path, 0, 0);

	return 1;
}