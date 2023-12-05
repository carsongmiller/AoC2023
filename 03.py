from timeit import default_timer as timer

lines = str()
with open('03.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	sum = 0
	for r in range(len(lines)):
		row = lines[r].strip()
		for c in range(len(row)):
			if not row[c].isnumeric() and row[c] != '.':
				# row[c] is a symbol
				coveredNeighbors = [
					[False, False, False],
					[False, False, False],
					[False, False, False]
					]
				#input doesn't have symbols on the edges
				rowAbove = lines[r-1].strip()
				rowBelow = lines[r+1].strip()

				if rowAbove[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c-1)
					sum += val
					coveredNeighbors[0][0] = True
					coveredNeighbors[0][1] = True
					if (travelRight >= 2): coveredNeighbors[0][2] = True
				
				if rowAbove[c].isnumeric() and not coveredNeighbors[0][1]:
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c)
					sum += val
					coveredNeighbors[0][0] = True
					coveredNeighbors[0][1] = True
					coveredNeighbors[0][2] = True
					
				if rowAbove[c+1].isnumeric() and not coveredNeighbors[0][2]:
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c+1)
					sum += val

				if row[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(row, c-1)
					sum += val

				if row[c+1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(row, c+1)
					sum += val

				if rowBelow[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c-1)
					sum += val
					coveredNeighbors[2][0] = True
					coveredNeighbors[2][1] = True
					if (travelRight >= 2): coveredNeighbors[2][2] = True
				
				if rowBelow[c].isnumeric() and not coveredNeighbors[2][1]:
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c)
					sum += val
					coveredNeighbors[2][0] = True
					coveredNeighbors[2][1] = True
					coveredNeighbors[2][2] = True
					
				if rowBelow[c+1].isnumeric() and not coveredNeighbors[2][2]:
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c+1)
					sum += val

	return sum

def part2(lines):
	sum = 0
	for r in range(len(lines)):
		row = lines[r].strip()
		for c in range(len(row)):
			if not row[c].isnumeric() and row[c] != '.':
				# row[c] is a symbol
				coveredNeighbors = [
					[False, False, False],
					[False, False, False],
					[False, False, False]
					]
				#input doesn't have symbols on the edges
				rowAbove = lines[r-1].strip()
				rowBelow = lines[r+1].strip()

				vals = []

				if rowAbove[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c-1)
					vals.append(val)
					coveredNeighbors[0][0] = True
					coveredNeighbors[0][1] = True
					if (travelRight >= 2): coveredNeighbors[0][2] = True
				
				if rowAbove[c].isnumeric() and not coveredNeighbors[0][1]:
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c)
					vals.append(val)
					coveredNeighbors[0][0] = True
					coveredNeighbors[0][1] = True
					coveredNeighbors[0][2] = True
					
				if rowAbove[c+1].isnumeric() and not coveredNeighbors[0][2]:
					val, travelLeft, travelRight = getContiguousNumber(rowAbove, c+1)
					vals.append(val)

				if row[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(row, c-1)
					vals.append(val)

				if row[c+1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(row, c+1)
					vals.append(val)

				if rowBelow[c-1].isnumeric():
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c-1)
					vals.append(val)
					coveredNeighbors[2][0] = True
					coveredNeighbors[2][1] = True
					if (travelRight >= 2): coveredNeighbors[2][2] = True
				
				if rowBelow[c].isnumeric() and not coveredNeighbors[2][1]:
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c)
					vals.append(val)
					coveredNeighbors[2][0] = True
					coveredNeighbors[2][1] = True
					coveredNeighbors[2][2] = True
					
				if rowBelow[c+1].isnumeric() and not coveredNeighbors[2][2]:
					val, travelLeft, travelRight = getContiguousNumber(rowBelow, c+1)
					vals.append(val)

				if len(vals) == 2:
					sum += vals[0] * vals[1]

	return sum

def getContiguousNumber(searchStr, startIndex):
	s = searchStr[startIndex]
	travelLeft = 0
	travelRight = 0
	# search left
	pos = startIndex - 1
	while(pos >= 0 and searchStr[pos].isnumeric()):
		s = searchStr[pos] + s
		travelLeft += 1
		pos -= 1
	
	# search right
	pos = startIndex + 1
	while(pos < len(searchStr) and searchStr[pos].isnumeric()):
		s = s + searchStr[pos]
		travelRight += 1
		pos += 1

	return int(s), travelLeft, travelRight

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