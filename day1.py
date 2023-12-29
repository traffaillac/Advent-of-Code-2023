from sys import stdin

# print(sum(int(next(c for c in l if c.isdigit()) + next(c for c in reversed(l) if c.isdigit())) for l in stdin))
W = tuple(enumerate("0123456789")) + tuple(enumerate("zero one two three four five six seven eight nine".split()))
print(sum(int(min((l.find(w), str(n)) for n, w in W if w in l)[1] + max((l.rfind(w), str(n)) for n, w in W if w in l)[1]) for l in stdin))
