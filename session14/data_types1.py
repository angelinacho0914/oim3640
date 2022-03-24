
  69: >>> counter.keys()
dict_keys(['r', 'a', 'p', 'h', 'e', 'l', ' ', 'm'])
  70: >>> counter
{'r': 2, 'a': 2, 'p': 2, 'h': 1, 'e': 2, 'l': 1, ' ': 1, 'm': 1}
  71:
>>> for k in counter.keys():
...     print(k)
...
  72:
>>> for v in counter.values():
...     print(v)
...
  73:
>>> for k, v in counter.items():
...     print(k, v)
...
  74: >>> d = {}
  75: >>> d['ab'] = 12
  76: >>> d['cd'] = 34
  77: >>> d
{'ab': 12, 'cd': 34}
  78: >>> d2 = {}
  79: >>> a = ['a', 'b']
  80: >>> d2[a] = 12
  81: >>> d2[tuple(a)] =  12
  82: >>> d2
{('a', 'b'): 12}
  83: >>> name
'raphael prem'
  84: >>> name.reversed()
  85: >>> name.reverse()
  86: >>> lst
[2, 2, 2, 1, 2, 1, 1, 1]
  87: >>> lst = list(name)
  88: >>> lst
['r', 'a', 'p', 'h', 'a', 'e', 'l', ' ', 'p', 'r', 'e', 'm']
  89: >>> lst.reverse()
  90: >>> lst
['m', 'e', 'r', 'p', ' ', 'l', 'e', 'a', 'h', 'p', 'a', 'r']
  91: >>> name[::-1]
'merp leahpar'
  92: >>> name
'raphael prem'
  93: >>> sorted(name)
[' ', 'a', 'a', 'e', 'e', 'h', 'l', 'm', 'p', 'p', 'r', 'r']
  94: >>> ''.join(sorted(name))
' aaeehlmpprr'
  95: >>> tuple(sorted(name))
(' ', 'a', 'a', 'e', 'e', 'h', 'l', 'm', 'p', 'p', 'r', 'r')
  96: >>> sorted('spot')
['o', 'p', 's', 't']
  97: >>> ''.join(sorted('spot'))
'opst'
  98: >>> ''.join(sorted('pots'))
'opst'
  99: >>> counter
{'r': 2, 'a': 2, 'p': 2, 'h': 1, 'e': 2, 'l': 1, ' ': 1, 'm': 1}