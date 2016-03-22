import random
import time

def countWater(minHeights, level):
	totalWater = 0
	for i in range(0, len(minHeights) - 1):
		totalWater += minHeights[i + 1] - minHeights[i] - 1
	return totalWater

def buildTable(heights, heightList, level):
	newList = [index for index in heightList if heights[index] >= level]
	return newList

def answer(heights):
	total = 0
	heightList = [i for i in range(0, len(heights))]
	for i in range(2, max(heights) + 1):
		heightList = buildTable(heights, heightList, i)
		total += countWater(heightList, i)
	return total

h = [1, 4, 2, 5, 1, 2, 3]
j = [1, 2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]

print answer(h)
print answer(j)

