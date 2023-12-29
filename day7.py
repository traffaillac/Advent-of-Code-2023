from collections import Counter
from sys import stdin

hands = []
for l in stdin:
	cards, bid = l.split()
	v = sorted(Counter(cards.replace('J','')).values())
	if not v:
		v.append(0)
	v[-1] += cards.count('J')
	type = 0
	if 5 in v:
		type = 6
	elif 4 in v:
		type = 5
	elif v == [2, 3]:
		type = 4
	elif 3 in v:
		type = 3
	elif v == [1, 2, 2]:
		type = 2
	elif 2 in v:
		type = 1
	hands.append((type, *("J23456789TQKA".index(c) for c in cards), int(bid)))
hands.sort()
print(sum((rank+1)*bid for rank,(_,_,_,_,_,_,bid) in enumerate(hands)))