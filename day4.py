from sys import stdin

L = stdin.read().split('\n')
cards = [1] * len(L)
for i, l in enumerate(L):
	win, have = (set(map(int, s.split())) for s in l.split(':')[1].split('|'))
	n = len(win & have)
	for j in range(n):
		cards[i+1+j] += cards[i]
print(sum(cards))