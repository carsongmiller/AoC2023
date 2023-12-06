from timeit import default_timer as timer
from math import floor, ceil

lines = str()
with open('06.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	rawTimes = lines[0].split(":")[1].strip().split(' ')
	rawDistances = lines[1].split(":")[1].strip().split(' ')
	times = []
	distances = []

	for rawTime in rawTimes:
		if rawTime.isnumeric():
			times.append(int(rawTime))

	for rawDistance in rawDistances:
		if rawDistance.isnumeric():
			distances.append(int(rawDistance))

	product = 1

	for raceIndex in range(len(times)):
		product *= getNumWins(times[raceIndex], distances[raceIndex])

	return product

def part2(lines):
	raceDuration = int(lines[0].replace('Time:', '').replace(' ', '').strip())
	distToBeat = int(lines[1].replace('Distance:', '').replace(' ', '').strip())
	return getNumWins(raceDuration, distToBeat)


def getDistance(raceDuration, chargeTime):
	return (raceDuration - chargeTime) * chargeTime

def getNumWins(raceDuration, distToBeat):
	for chargeTime in range(raceDuration):
		if getDistance(raceDuration, chargeTime) > distToBeat:
			return (((raceDuration + 1)/2) - chargeTime) * 2


dur = 17
for i in range(dur + 1):
	print(str(i) + '\t' + str(getDistance(dur, i)))


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