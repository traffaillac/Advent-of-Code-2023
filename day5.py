S = list(map(int, input()[7:].split()))
seeds = list(zip(S[0::2], S[1::2]))
input()
for i in range(7):
	input()
	R = []
	while True:
		S = input()
		if S == '': break
		R.append(tuple(map(int, S.split())))
	new = []
	while seeds:
		s, t = seeds.pop()
		dst, src, n = next(((dst, src, n) for dst, src, n in R if src<s+t and s<src+n), (s, s, t))
		a, b = max(s, src), min(s+t, src+n)
		new.append((a-src+dst, b-a))
		if a > s:
			seeds.append((s, a-s))
		if b < s+t:
			seeds.append((b, s+t-b))
	seeds = new
print(min(seeds)[0])