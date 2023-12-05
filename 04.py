from timeit import default_timer as timer

lines = str()
with open('04.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	score = 0
	for line in lines:
		wins = countWins(line.strip())
		score += pow(2, wins - 1) if wins > 0 else 0

	return score
	

def part2(lines):
	cards = {}
	for i in range(len(lines)):
		cards[i] = 1

	for cardIndex in range(len(lines)):
		currentCard = lines[cardIndex].strip()
		wins = countWins(currentCard)
		for i in range(cardIndex + 1, cardIndex + wins + 1, 1):
			cards[i] += cards[cardIndex]

	cardCount = 0
	for value in cards.values():
		cardCount += value
		
	return cardCount

def countWins(card):
	wins = 0
	card = card.split(": ")[1]
	winners, nums = card.split(" | ")
	winners = winners.split(" ")
	nums = nums.split(" ")
	for winner in winners:
		wins += 1 if winner.isnumeric() and winner in nums else 0
	
	return wins

	

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