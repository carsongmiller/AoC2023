from timeit import default_timer as timer
from itertools import cycle
import math

lines = str()
with open('08.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	directions = lines[0].strip()
	nodes = {}
	for line in lines[2:]:
		nodes[line[0:3]] = (line[7:10], line[12:15])


	step = 0
	loc = "AAA"
	while loc != "ZZZ":
		dir = directions[step % len(directions)]
		if dir == 'L':
			loc = nodes[loc][0]
		else:
			loc = nodes[loc][1]
			
		step += 1
	return step

def part2(lines):
	directions = [0 if d == 'L' else 1 for d in lines[0].strip()]
	nodes = {}
	for line in lines[2:]:
		nodes[line[0:3]] = [line[7:10], line[12:15]]

	startNodes = [node for node in nodes if node[2] == 'A']
	
	#find the steps required to get from each end node back to itself
	fullLoopSteps = {}
	cycleSteps = []
	for startNode in startNodes:
		loc = startNode
		for step, d in enumerate(cycle(directions), start=1):
			loc = nodes[loc][d]
			if loc[2] == 'Z':
				cycleSteps.append(step)
				break

	return math.lcm(*cycleSteps)


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