from timeit import default_timer as timer

lines = str()
with open('01.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	sum = 0
	for line in lines:
		# find first digit
		leftChar = 'x'
		rightChar = 'x'

		for leftIndex in range(len(line)):
			if line[leftIndex].isnumeric():
				leftChar = line[leftIndex]
				break
		for rightIndex in range(len(line) - 1, -1, -1):
			if line[rightIndex].isnumeric():
				rightChar = line[rightIndex]
				break

		sum += (int)(leftChar + rightChar)

	return sum

def part2(lines):
	sum = 0
	for line in lines:
		leftValue = findLeftMostNumber(line)
		rightValue = findRightMostNumber(line)
		sum += int(str(leftValue) + str(rightValue))
	return sum


def findLeftMostNumber(line):
	bestIndex = len(line)
	value = 0
	for leftIndex in range(len(line)):
		if line[leftIndex].isnumeric():
			bestIndex = leftIndex
			value = int(line[leftIndex])
			break

	if bestIndex <= 2:
		return value
	
	#now search for spelled out words

	place = line.find("one")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 1

	place = line.find("two")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 2
	
	place = line.find("three")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 3

	place = line.find("four")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 4

	place = line.find("five")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 5

	place = line.find("six")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 6

	place = line.find("seven")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 7

	place = line.find("eight")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 8

	place = line.find("nine")
	if (place < bestIndex and place != -1):
		bestIndex = place
		value = 9

	return value

def findRightMostNumber(line):
	bestIndex = len(line)
	value = 0
	for rightIndex in range(len(line) - 1, -1, -1):
		if line[rightIndex].isnumeric():
			bestIndex = rightIndex
			value = int(line[rightIndex])
			break

	if bestIndex >= len(line) - 3:
		return value
	
	#now search for spelled out words

	place = line.rfind("one")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 1

	place = line.rfind("two")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 2
	
	place = line.rfind("three")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 3

	place = line.rfind("four")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 4

	place = line.rfind("five")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 5

	place = line.rfind("six")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 6

	place = line.rfind("seven")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 7

	place = line.rfind("eight")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 8

	place = line.rfind("nine")
	if (place > bestIndex and place != -1):
		bestIndex = place
		value = 9

	return value


start = timer()
p1 = part1(lines)
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(lines)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()