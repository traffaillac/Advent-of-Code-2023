from collections import defaultdict
from string import ascii_letters

boxes = defaultdict(dict)
for s in input().split(','):
	b = 0
	for c in s:
		if c in ascii_letters:
			b = (b + ord(c)) * 17 % 256
	if s[-1] == '-':
		boxes[b].pop(s[:-1], None)
	else:
		label, lens = s.split('=')
		boxes[b][label] = int(lens)
print(sum((b+1)*sum((i+1)*l for i, l in enumerate(box.values())) for b, box in boxes.items()))