from math import gcd
from sys import stdin

D = ((0,1), (1,0), (0,-1), (-1,0))
P = [(0,0)]
for l in stdin:
	col = l.split()[2]
	dr, dc = D[int(col[7])]
	m = int(col[2:7], 16)
	P.append((P[-1][0]+dr*m,P[-1][1]+dc*m))
a, p = 0, 0
for (r0,c0),(r1,c1) in zip(P,P[1:]):
	a += r0*c1-r1*c0
	p += abs(r0-r1)+abs(c0-c1)
print(abs(a)//2+p//2+1)