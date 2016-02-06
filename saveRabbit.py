inf = float("inf")

def answer(food, grid):
	memo = [[inf for col in row] for row in grid]
	ans = []
	traverse(food, grid, 0, 0, memo, ans)
	if ans:
		return min(ans)
	else:
		return -1


def traverse(food, grid, row, col, memo, ans):
	currFood = food - grid[row][col]
	if currFood < 0:
		return
	if currFood < memo[row][col]:
		memo[row][col] = currFood
	else:
		return
	if row == len(grid) - 1 and col == len(grid[0]) - 1:
		ans.append(currFood)
		return
	if row < (len(grid) - 1):
		traverse(currFood, grid, row + 1, col, memo, ans)
	if col < (len(grid[0]) - 1):
		traverse(currFood, grid, row, col + 1, memo, ans)

food1 = 7
grid1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]

food2 = 12
grid2 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]


print answer(food2, grid2)