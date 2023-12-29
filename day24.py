from pprint import pprint
from sys import stdin
from z3 import *

hails = []
for l in stdin:
	a, b = l.split(" @ ")
	hails.append((*map(int, a.split(", ")), *map(int, b.split(", "))))
cross = 0
for i,(x0,y0,z0,d0,e0,f0) in enumerate(hails):
	for j,(x1,y1,z1,d1,e1,f1) in enumerate(hails):
		div = d0*e1-e0*d1
		if div != 0:
			t = ((y0-y1)*d1-(x0-x1)*e1)/div
			u = ((y0-y1)*d0-(x0-x1)*e0)/div
			x, y = x0+d0*t, y0+e0*t
			if t>=0 and u>=0 and 200000000000000<=x<=400000000000000 and 200000000000000<=y<=400000000000000:
				cross += 1
print(cross//2)

x0, y0, z0, dx0, dy0, dz0 = hails[0]
x1, y1, z1, dx1, dy1, dz1 = hails[1]
x2, y2, z2, dx2, dy2, dz2 = hails[2]
x, y, z, dx, dy, dz, t, u, v = Reals("x y z dx dy dz t u v")
solve(t>=0, u>=0, v>=0,
	x+dx*t==x0+dx0*t, y+dy*t==y0+dy0*t, z+dz*t==z0+dz0*t,
	x+dx*u==x1+dx1*u, y+dy*u==y1+dy1*u, z+dz*u==z1+dz1*u,
	x+dx*v==x2+dx2*v, y+dy*v==y2+dy2*v, z+dz*v==z2+dz2*v)
