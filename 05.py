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
		transformedSets.append([traceThroughMap_Range(transformedSets[-1], maps[-1])])


	return


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
	destSet = []
	for set in sourceSets:
		sourceStart = set[0]
		sourceRange = set[1]

		for entry in map:
			mapSourceStart = entry[1]
			mapDestStart = entry[0]
			mapRange = entry[2]

			# source range does not overlap with map at all
			if (sourceStart + sourceRange <= mapSourceStart) or (sourceStart >= mapSourceStart + mapRange):
				destSet.append([sourceStart, sourceRange])
			
			#source and map perfectly align
			elif (sourceStart == mapSourceStart) and (sourceRange == mapRange):
				destSet.append([mapDestStart, mapRange])

			# source completely surrounds map
			elif (sourceStart <= mapSourceStart) and (sourceStart + sourceRange >= mapSourceStart + mapRange):
				destSet.append([sourceStart, mapSourceStart - sourceStart])
				destSet.append([mapDestStart, mapRange])
				destSet.append([mapSourceStart + mapRange, sourceRange - mapRange - (mapSourceStart - sourceStart)])

			# source overlaps only on the low side of the map
			elif (sourceStart < mapSourceStart) and (sourceStart + sourceRange < mapSourceStart + mapRange):
				destSet.append([sourceStart, mapSourceStart - sourceStart])
				destSet.append([mapDestStart, sourceRange - (mapSourceStart - sourceStart)])

			# source overlaps only on the high side of the map
			elif (sourceStart >= mapSourceStart) and (sourceStart + sourceRange > mapSourceStart + mapRange):
				destSet.append([mapDestStart + (sourceStart - mapSourceStart), mapRange - (sourceStart - mapSourceStart)])
				destSet.append([mapSourceStart + mapRange, sourceRange - (mapRange - (sourceStart - mapSourceStart))])

			# source lies completely within the map
			elif (sourceStart >= mapSourceStart) and (sourceStart + sourceRange <= mapSourceStart + mapRange):
				destSet.append([mapDestStart + (sourceStart - mapSourceStart), sourceRange])
			
			else:
				print("Shouldn't be here")
			

	return destSet





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