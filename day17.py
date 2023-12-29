from heapq import heappush, heappop
from sys import stdin

G = [list(map(int, l)) for l in stdin.read().split()]
R, C = len(G), len(G[0])
H = sorted(((G[0][1], 0, 1, 0, 1, 1), (G[1][0], 1, 0, 1, 0, 1)))
starts = {(0, 0, 0, 1), (0, 0, 1, 0)}
while H and not(H[0][1]==R-1 and H[0][2]==C-1 and H[0][5]>=4):
	l, r, c, dr, dc, b = heappop(H)
	lr, lc = r-dc, c+dr
	if b>=4 and 0<=lr<R and 0<=lc<C and (r, c, -dc, dr) not in starts:
		starts.add((r, c, -dc, dr))
		heappush(H, (l+G[lr][lc], lr, lc, -dc, dr, 1))
	rr, rc = r+dc, c-dr
	if b>=4 and 0<=rr<R and 0<=rc<C and (r, c, dc, -dr) not in starts:
		starts.add((r, c, dc, -dr))
		heappush(H, (l+G[rr][rc], rr, rc, dc, -dr, 1))
	fr, fc = r+dr, c+dc
	if b<10 and 0<=fr<R and 0<=fc<C:
		heappush(H, (l+G[fr][fc], fr, fc, dr, dc, b+1))
print(H[0][0])