from timeit import default_timer as timer

lines = str()
with open('09.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	lines = [[int(x) for x in line.split(' ')] for line in lines]
	sum = 0
	for line in lines:
		sum += getNextValue(line)
	return sum

def part2(lines):
	lines = [[int(x) for x in line.split(' ')] for line in lines]
	sum = 0
	for line in lines:
		sum += getPrevValue(line)
	return sum

def getNextValue(sequence: list) -> int:
	if sequence.count(0) == len(sequence):
		# terminal case
		return 0
	
	diffList = []
	for i in range(len(sequence) - 1):
		diffList.append(sequence[i + 1] - sequence[i])
	
	return sequence[-1] + getNextValue(diffList)

def getPrevValue(sequence: list) -> int:
	if sequence.count(0) == len(sequence):
		# terminal case
		return 0
	
	diffList = []
	for i in range(len(sequence) - 1):
		diffList.append(sequence[i + 1] - sequence[i])
	
	return sequence[0] - getPrevValue(diffList)

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