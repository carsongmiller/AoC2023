from timeit import default_timer as timer

lines = str()
with open('05.txt') as f:
	lines = f.read()

def part1(lines):
	sections = lines.split("\n\n")
	for i in range(len(sections)):
		sections[i] = sections[i].split(":")[1].strip()
	
	seeds = [int(x) for x in sections[0].split(' ')]
	seedToSoil = createMap(sections[1].split('\n'))
	soilToFertilizer = createMap(sections[2].split('\n'))
	fertilizerToWater = createMap(sections[3].split('\n'))
	waterToLight = createMap(sections[4].split('\n'))
	lightToTemperature = createMap(sections[5].split('\n'))
	temperatureToHumidity = createMap(sections[6].split('\n'))
	humidityToLocation = createMap(sections[7].split('\n'))
	
	closest = 1000000000000000

	for seed in seeds:
		# track the seed through all the maps and find location
		dest = seed
		dest = traceThroughMap_Single(dest, seedToSoil)
		dest = traceThroughMap_Single(dest, soilToFertilizer)
		dest = traceThroughMap_Single(dest, fertilizerToWater)
		dest = traceThroughMap_Single(dest, waterToLight)
		dest = traceThroughMap_Single(dest, lightToTemperature)
		dest = traceThroughMap_Single(dest, temperatureToHumidity)
		dest = traceThroughMap_Single(dest, humidityToLocation)

		closest = min(dest, closest)

	return closest

def part2(lines):
	sections = lines.split("\n\n")
	for i in range(len(sections)):
		sections[i] = sections[i].split(":")[1].strip()
	
	originalSeedSets = [int(x) for x in sections[0].split(' ')]
	transformedSets = [[]]
	for i in range(0, len(originalSeedSets), 2):
		transformedSets[0].append([originalSeedSets[i], originalSeedSets[i+1]])

	maps = []

	for i in range(len(sections) - 1):
		maps.append(createMap(sections[i + 1].split('\n')))
		transformedSets.append(traceThroughMap_Range(transformedSets[-1], maps[-1]))


	s = [x[0] for x in transformedSets[-1]]
	m = min(s)

	return m


def createMap(rawMapData):
	map = []
	for i in range(len(rawMapData)):
		map.append([int(x) for x in rawMapData[i].split(' ')])
	return map

def traceThroughMap_Single(source, map):
	dest = source
	for entry in map:
		mapSourceStart = entry[1]
		mapDestStart = entry[0]
		mapRange = entry[2]

		if mapSourceStart <= source < mapSourceStart + mapRange:
			return mapDestStart + source - mapSourceStart

	return source

def traceThroughMap_Range(sourceSets, map):
	mappedSets = []

	for sourceSet in sourceSets:
		setsInProcess = [sourceSet]

		while setsInProcess:
			currentSource = setsInProcess.pop()
			sourceStart = currentSource[0]
			sourceRange = currentSource[1]
			sourceEnd = sourceStart + sourceRange - 1

			mapped = False

			for mapSection in map:
				# for each map, check if the source overlaps with it at all
				mapSourceStart = mapSection[1]
				mapDestStart = mapSection[0]
				mapRange = mapSection[2]
				mapSourceEnd = mapSourceStart + mapRange - 1
				
				if not (sourceEnd < mapSourceStart or sourceStart > mapSourceEnd):
					# we've got some mapping to do
					mapped = True
					
					if sourceStart < mapSourceStart:
						# the unmapped chunk of the source range which lies before the map
						setsInProcess.append([sourceStart, mapSourceStart - sourceStart])
					if sourceEnd > mapSourceEnd:
						# the unmapped chunk of the source range which lies after the map
						setsInProcess.append([mapSourceEnd + 1, sourceEnd - mapSourceEnd])
					
					if sourceStart >= mapSourceStart and sourceEnd <= mapSourceEnd:
						# the source range lies completely within the map
						mappedSets.append([mapDestStart + (sourceStart - mapSourceStart), sourceRange])
					
					elif sourceStart < mapSourceStart and sourceEnd > mapSourceEnd:
						# the source lies completely AROUND the map (the whole map range must be added)
						mappedSets.append([mapDestStart, mapRange])

					elif sourceEnd <= mapSourceEnd:
						# the source starts before the map, and ends before or right with it
						mappedSets.append([mapDestStart, sourceEnd - mapSourceStart])
					
					elif sourceStart >= mapSourceStart:
						# the source starts within the map, and ends after it
						mappedSets.append([mapDestStart + (sourceStart - mapSourceStart), mapSourceEnd - sourceStart])
			
			if not mapped:
				mappedSets.append([sourceStart, sourceRange])
			
	return mappedSets





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