from sys import stdin
from functools import cache

# res = 0
# for l in stdin:
# 	spr, dam = l.split()
# 	dam = list(map(int, dam.split(',')))
# 	arr = 0
# 	for holes in product(range(len(spr)-sum(dam)-len(dam)+3), repeat=len(dam)+1):
# 		if sum(holes)+sum(dam)==len(spr) and all(h>0 for h in holes[1:-1]):
# 			cand = ''.join('.'*a+'#'*b for a, b in zip(holes, dam+[0]))
# 			arr += all(s=='?' or s==c for s, c in zip(spr, cand))
# 	res += arr
# print(res)

@cache
def arr(spr, dam):
	if len(spr)==0:
		return len(dam)==0
	res = 0
	if dam and len(spr)>=dam[-1] and all(spr[~i]!='.' for i in range(dam[-1])) and (len(spr)==dam[-1] or spr[~dam[-1]]!='#'):
		res += arr(spr[:~dam[-1]], dam[:-1])
	if spr[-1]!='#':
		res += arr(spr[:-1], dam)
	return res

S = 0
for l in stdin:
	spr, dam = l.split()
	dam = tuple(map(int, dam.split(',')))
	S += arr('?'.join([spr]*5), dam*5)
print(S)