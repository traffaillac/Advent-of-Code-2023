from collections import defaultdict
from functools import reduce
from operator import mul

W = defaultdict(list)
while True:
	l = input()
	if l == '': break
	name, rules = l[:-1].split('{')
	for rule in rules.split(','):
		if ':' in rule:
			W[name].append(("xmas".index(rule[0]), rule[1], int(rule[2:rule.index(':')]), rule[rule.index(':')+1:]))
		else:
			W[name].append((0, '>', 0, rule))

# part 1
r = 0
while True:
	try: l = input()
	except: break
	t = tuple(int(s[2:]) for s in l[1:-1].split(','))
	w = "in"
	while w!='A' and w!='R':
		for i, op, v, dst in W[w]:
			if op=='<' and t[i]<v or op=='>' and t[i]>v:
				w = dst
				break
	if w == 'A':
		r += sum(t)
print(r)

# part 2
S = [("in",[(1,4001),(1,4001),(1,4001),(1,4001)])]
r = 0
while S:
	w, ints = S.pop()
	if w == 'A':
		r += reduce(mul, (M-m for m, M in ints), 1)
	elif w != 'R':
		for i, op, v, dst in W[w]:
			m, M = ints[i]
			if op=='<' and m<v or op=='>' and M-1>v:
				ints[i] = (m,min(M,v)) if op=='<' else (max(m,v+1),M)
				S.append((dst, ints[:]))
				ints[i] = (v,M) if op=='<' else (m,v+1)
				if ints[i][0]>=ints[i][1]: break
print(r)