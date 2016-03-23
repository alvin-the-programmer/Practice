def answer(heights):
	totalWater = 0
	i = 0
	while i < len(heights) - 1:
		lMax = i
		# (height, index)
		rMax = (0, -1)
		if heights[i] > 1:
			for j in range(i + 1, len(heights)):
				if heights[j] >= heights[lMax]:
					rMax = (heights[j], j)
					i = j - 1
					break
				elif heights[j] >= rMax[0]:
					rMax = (heights[j], j)
					i = j - 1
			totalWater += getVolume(heights, lMax, rMax[1])
		i += 1
	return totalWater

def getVolume(heights, i, j):
	displacement = 0
	for height in heights[i + 1:j]:
		displacement += height
	volume =  min([heights[i], heights[j]]) * (j - i - 1)
	return volume - displacement