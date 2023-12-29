# T = map(int, input()[11:].split())
# D = map(int, input()[11:].split())
# w = 1
# for t, d in zip(T, D):
# 	w *= sum(b*(t-b)>d for b in range(1, t))
from math import sqrt, ceil
t = int(input()[11:].replace(' ', ''))
d = int(input()[11:].replace(' ', ''))
sq = sqrt(t*t-4*d)
print(ceil((t+sq)/2-1) - int((t-sq)/2+1) + 1)
