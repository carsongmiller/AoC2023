from timeit import default_timer as timer
from enum import Enum
from functools import cmp_to_key
from itertools import combinations_with_replacement

lines = str()
with open('07.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

replacementHands = {}

def part1(lines):
	handsWithBids = {}
	for line in lines:
		hand, bid = line.split(' ')
		handsWithBids[hand] = int(bid)
	
	hands = list(handsWithBids.keys())
	hands.sort(key=cmp_to_key(compareHands_Part1), reverse=True)
	handsWithBidsSorted = {i: handsWithBids[i] for i in hands}

	winnings = 0
	vals = list(handsWithBidsSorted.values())
	for i in range(len(handsWithBidsSorted)):
		winnings += (i + 1) * vals[i]

	return winnings

def part2(lines):
	handsWithBids = {}
	for line in lines:
		hand, bid = line.split(' ')
		if 'J' in hand:
			# see what card(s) we could replace the jokers with to maximize this hand's score
			cardCandidates = set(hand.replace('J', ''))
			if len(cardCandidates) == 0:
				# it was all jokers
				cardCandidates = {'A'}
			handCandidates = generateHandCandidates(hand, cardCandidates)
			handCandidates.sort(key=cmp_to_key(compareHands_Part1))
			replacementHands[hand] = handCandidates[0] #keep a dict of the best hand for all joker hands

		handsWithBids[hand] = int(bid)
	
	hands = list(handsWithBids.keys())
	hands.sort(key=cmp_to_key(compareHands_Part2), reverse=True)
	handsWithBidsSorted = {i: handsWithBids[i] for i in hands}

	winnings = 0
	vals = list(handsWithBidsSorted.values())
	for i in range(len(handsWithBidsSorted)):
		winnings += (i + 1) * vals[i]

	return winnings

def cardValue(card):
	if card.isnumeric():
		return int(card)
	elif card == 'A':
		return 14
	elif card == 'K':
		return 13
	elif card == 'Q':
		return 12
	elif card == 'J':
		return 11
	elif card == 'T':
		return 10
	
def handClass(hand: str):
	cardDict = {}

	for card in hand:
		if not card in cardDict:
			cardDict[card] = 0
		cardDict[card] += 1

	sortedList = sorted(cardDict, key=lambda x: cardDict[x])
	
	if cardDict[sortedList[-1]] == 5:
		return HandTypes.fiveOfAKind
	elif cardDict[sortedList[-1]] == 4:
		return HandTypes.fourOfAKind
	elif cardDict[sortedList[-1]] == 3:
		if cardDict[sortedList[-2]] == 2:
			return HandTypes.fullHouse
		else:
			return HandTypes.threeOfAKind
	elif cardDict[sortedList[-1]] == 2:
		if cardDict[sortedList[-2]] == 2:
			return HandTypes.twoPair
		else:
			return HandTypes.onePair
	else:
		return HandTypes.highCard

class HandTypes(Enum):
	highCard = 0
	onePair = 1
	twoPair = 2
	threeOfAKind = 3
	fullHouse = 4
	fourOfAKind = 5
	fiveOfAKind = 6

def compareHandsCardwise(handA, handB):
	for i in range(len(handA)):
		if cardValue(handA[i]) > cardValue(handB[i]):
			return -1
		elif cardValue(handA[i]) < cardValue(handB[i]):
			return 1
	return 0

def compareHands_Part1(handA, handB):
	classA = handClass(handA)
	classB = handClass(handB)
	if classA.value > classB.value:
		return -1
	elif classA.value < classB.value:
		return 1
	else:
		return compareHandsCardwise(handA, handB)
	
def compareHands_Part2(handA, handB):
	if handA in replacementHands.keys():
		classA = handClass(replacementHands[handA])
	else:
		classA = handClass(handA)
	
	if handB in replacementHands.keys():
		classB = handClass(replacementHands[handB])
	else:
		classB = handClass(handB)

	if classA.value > classB.value:
		return -1
	elif classA.value < classB.value:
		return 1
	else:
		return compareHandsCardwise(handA, handB)

def generateHandCandidates(hand, cardCandidates):
	handCandidates = []
	newHand = hand.replace('J','')
	for replacement in combinations_with_replacement(cardCandidates, hand.count('J')):
		handCandidates.append(newHand + ''.join(replacement))

	return handCandidates

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