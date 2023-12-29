from sys import stdin

s = 0
for l in stdin:
	hist = [list(map(int, l.split()))]
	while any(d!=0 for d in hist[-1]):
		hist.append([b-a for a, b in zip(hist[-1],hist[-1][1:])])
	s += sum(h[0]*(-1)**i for i, h in enumerate(hist))
print(s)