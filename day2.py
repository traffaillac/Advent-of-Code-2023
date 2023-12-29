from sys import stdin

s = 0
for g, L in enumerate(stdin):
	m = {"red": 0, "green": 0, "blue": 0}
	for M in L.split(':')[1].split(';'):
		for N in M.split(','):
			n, c = N.split()
			m[c] = max(m[c], int(n))
	s += m["red"] * m["green"] * m["blue"]
print(s)
