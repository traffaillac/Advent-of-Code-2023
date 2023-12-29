from collections import deque
from sys import stdin

nb = ((-1, 0), (0, -1), (0, 1), (1, 0))
G = stdin.read().split()
N = len(G)
S = 589 # 327->95262, 589->308232, 851->642778, 1113->1098900
rs, cs = next((r, c) for r, g in enumerate(G) for c, a in enumerate(g) if a=='S')
visited = {(rs, cs): 0}
queue = deque([(rs, cs)])
while queue:
	r, c = queue.popleft()
	for dr, dc in nb:
		i, j = r+dr, c+dc
		if G[i%N][j%N]!='#' and (i, j) not in visited and visited[r, c]<S:
			visited[i, j] = visited[r, c] + 1
			queue.append((i, j))
nw0 = sum(rs-262<=r<rs and cs-262<=c<cs and v%2==S%2 for (r, c), v in visited.items())
nw1 = sum(rs-262<=r<rs and cs-524<=c<cs-262 and v%2==S%2 for (r, c), v in visited.items())
nw2 = sum(rs-262<=r<rs and c<cs-524 and v%2==S%2 for (r, c), v in visited.items())
ne0 = sum(cs<c<=cs+262 and rs-262<=r<rs and v%2==S%2 for (r, c), v in visited.items())
ne1 = sum(cs<c<=cs+262 and rs-524<=r<rs-262 and v%2==S%2 for (r, c), v in visited.items())
ne2 = sum(cs<c<=cs+262 and r<rs-524 and v%2==S%2 for (r, c), v in visited.items())
sw0 = sum(cs-262<=c<cs and rs<r<=rs+262 and v%2==S%2 for (r, c), v in visited.items())
sw1 = sum(cs-262<=c<cs and rs+262<r<=rs+524 and v%2==S%2 for (r, c), v in visited.items())
sw2 = sum(cs-262<=c<cs and rs+524<r and v%2==S%2 for (r, c), v in visited.items())
se0 = sum(rs<r<=rs+262 and cs<c<=cs+262 and v%2==S%2 for (r, c), v in visited.items())
se1 = sum(rs<r<=rs+262 and cs+262<c<=cs+524 and v%2==S%2 for (r, c), v in visited.items())
se2 = sum(rs<r<=rs+262 and cs+524<c and v%2==S%2 for (r, c), v in visited.items())
T = 26501365
div = T//262
print((nw0+ne0+sw0+se0)*div*(div-1)//2+(nw1+ne1+sw1+se1)*div+(nw2+ne2+sw2+se2)*(div+1)+(T+1)//2*4)