from timeit import default_timer as timer

lines = str()
with open('02.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	limitR = 12
	limitG = 13
	limitB = 14
	gameIndex = 0
	sum = 0

	for game in lines:
		game = game.strip()
		gameID = int(game[5:game.find(":")])

		trials = game[game.find(": ") + 2:len(game)].split("; ")
		for trial in trials:
			possible = True
			colors = trial.split(", ")

			for item in colors:
				quant, color = item.split(" ")
				quant = int(quant)
				if ((color == "red" and quant > limitR) or 
					(color == "green" and quant > limitG) or 
					(color == "blue" and quant > limitB)):
					possible = False
					break

			if not possible:
				break
			
		if possible:
			sum += gameID

	return sum	

def part2(lines):
	limitR = 12
	limitG = 13
	limitB = 14
	gameIndex = 0
	sum = 0

	for game in lines:
		game = game.strip()
		gameID = int(game[5:game.find(":")])
		minQuant = {
			"red":0,
			"green":0,
			"blue":0
		}

		trials = game[game.find(": ") + 2:len(game)].split("; ")

		for trial in trials:
			possible = True
			colors = trial.split(", ")

			for item in colors:
				quant, color = item.split(" ")
				minQuant[color] = max(int(quant), minQuant[color])
		
		sum += minQuant["red"] * minQuant["green"] * minQuant["blue"]
	return sum


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