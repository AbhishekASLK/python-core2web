from collections import defaultdict
import keyword, re

d = defaultdict(set)
for i, j in keyword.__builtins__.items():
  if not re.search('Error|Warning|__|ipython', i):
    d[type(eval(i).__init__)].add(i)

print(d)
