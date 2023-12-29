from collections import defaultdict, deque
from pprint import pprint
from sys import stdin

types = {}
dsts = {}
last = {}
srcs = defaultdict(list)
for l in stdin.read().split("\n"):
	src, dst = l.split(" -> ")
	name, dst = src[int(src[0].islower())^1:], dst.split(", ")
	types[name] = src[0]
	dsts[name] = dst
	last[name] = False
	for d in dst:
		srcs[d].append(name)

pulses = deque()
sent = [0, 0]
highs = defaultdict(list)
for i in range(40000):
	pulses.append(("broadcaster", False))
	sent[0] += 1
	while pulses:
		src, pulse = pulses.popleft()
		if src in ("gt", "vr", "nl", "lr") and pulse:
			highs[src].append(i)
		last[src] = pulse
		sent[pulse] += len(dsts[src])
		for dst in dsts[src]:
			if dst in types:
				if types[dst] == 'b':
					pulses.append((dst, pulse))
				elif types[dst] == '%':
					if not pulse:
						pulses.append((dst, not last[dst]))
				else:
					pulses.append((dst, not all(last[s] for s in srcs[dst])))
print(sent[0]*sent[1])
pprint(highs)
