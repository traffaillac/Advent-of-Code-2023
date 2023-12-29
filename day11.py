from sys import stdin

M = stdin.read().split()
erows = [r for r, R in enumerate(M) if not '#' in R]
ecols = [c for c in range(len(M[0])) if all(R[c]=='.' for R in M)]
gal = [(r, c) for r, R in enumerate(M) for c, C in enumerate(R) if C=='#']
s = 0
for i, (r0, c0) in enumerate(gal):
	for j in range(i+1, len(gal)):
		r1, c1 = gal[j]
		s += abs(r0-r1)+abs(c0-c1)+999999*(sum(r0<r<r1 for r in erows)+sum(c0<c<c1 or c1<c<c0 for c in ecols))
print(s)