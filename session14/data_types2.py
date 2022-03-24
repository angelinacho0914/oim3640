   1: >>> # string and list
   2: >>> name = 'alan xian'
   3: >>> lst = list(name)
   4: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
   5: >>> ''.join(lst)
'alan xian'
   6: >>> lst = name.split()
   7: >>> lst
['alan', 'xian']
   8: >>> ' '.join(lst)
'alan xian'
   9: >>> '-'.join(lst)
'alan-xian'
  10: >>> name
'alan xian'
  11: >>> name
'alan xian'
  12: >>> sorted(name)
[' ', 'a', 'a', 'a', 'i', 'l', 'n', 'n', 'x']
  13: >>> # string and dict
  14: >>> name
'alan xian'
  15: >>> d = {}
  16:
>>> for c in name:
...     d[c] = d.get(c, 0) + 1
...
  17: >>> d
{'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1}
  18: >>> from collections import Counter
  19: >>> counter = Counter(name)
  20: >>> counter
Counter({'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1})
  21: >>> # string and tuple
  22: >>> name
'alan xian'
  23: >>> t = tuple(name)
  24: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  25: >>> ''.join(t)
'alan xian'
  26: >>> # string and set
  27: >>> name
'alan xian'
  28: >>> s = set(name)
  29: >>> s
{' ', 'a', 'i', 'l', 'n', 'x'}
  30: >>> s[0]
  31: >>> # there is no order in set
  32: >>> # list and dict
  33: >>> lst
['alan', 'xian']
  34: >>> lst = list(name)
  35: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  36: >>> # similar to string and dictionary
  37: >>> # list and tuple
  38: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  39: >>> t = tuple(lst)
  40: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  41: >>> lst = list(t)
  42: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  43: >>> # list and set
  44: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  45: >>> s = set(lst)
  46: >>> s
{' ', 'a', 'i', 'l', 'n', 'x'}
  47: >>> # dictionary and tuple
  48: >>> d
{'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1}
  49: >>> # we could use tuple/string as keys in dict
  50: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  51: >>> d2[t] = 1
  52: >>> d2={}
  53: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  54: >>> d2[t] = 1
  55: >>> d2
{('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n'): 1}
  56: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  57: >>> d3 = {}
  58: >>> d3[lst] = 1
  59: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  60: >>> counter = Counter(t)
  61: >>> counter
Counter({'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1})
  62: >>> # string list and dictionary
  63: >>> d
{'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1}
  64:
>>> for k in d.keys():
...     print(k)
...
  65:
>>> for v in d.values():
...     print(v)
...
  66: >>> list(d.keys())
['a', 'l', 'n', ' ', 'x', 'i']
  67: >>> list(d.values())
[3, 1, 2, 1, 1, 1]
  68:
>>> for k, v in d.items():
...     print(k, v)
...
  69: >>> d
{'a': 3, 'l': 1, 'n': 2, ' ': 1, 'x': 1, 'i': 1}
  70: >>> d.keys()
dict_keys(['a', 'l', 'n', ' ', 'x', 'i'])
  71: >>> d.values()
dict_values([3, 1, 2, 1, 1, 1])
  72: >>> d.items()
dict_items([('a', 3), ('l', 1), ('n', 2), (' ', 1), ('x', 1), ('i', 1)])
  73: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  74:
>>> for i, letter in lst:
...     print(i, letter)
...
  75:
>>> for i, letter in enumerate(lst):
...     print(i, letter)
...
  76: >>> enumerate(lst)
<enumerate at 0x25affd34340>
  77: >>> list(enumerate(lst))
[(0, 'a'),
 (1, 'l'),
 (2, 'a'),
 (3, 'n'),
 (4, ' '),
 (5, 'x'),
 (6, 'i'),
 (7, 'a'),
 (8, 'n')]
  78: >>> name
'alan xian'
  79: >>> name[0] = 'e'
  80: >>> lst = list(name)
  81: >>> lst
['a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  82: >>> lst[0] = 'e'
  83: >>> ''.join(lst)
'elan xian'
  84: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  85: >>> t.sort()
  86: >>> lst
['e', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n']
  87: >>> lst.sort()
  88: >>> lst
[' ', 'a', 'a', 'e', 'i', 'l', 'n', 'n', 'x']
  89: >>> t
('a', 'l', 'a', 'n', ' ', 'x', 'i', 'a', 'n')
  90: >>> sorted(t)
[' ', 'a', 'a', 'a', 'i', 'l', 'n', 'n', 'x']
  91: >>> tuple(sorted(t))
(' ', 'a', 'a', 'a', 'i', 'l', 'n', 'n', 'x')
  92: >>> d = []
  93: >>> word1 = 'stop'
  94: >>> word2  = 'pots'
  95: >>> sorted(word1)
['o', 'p', 's', 't']
  96: >>> sorted(word2)
['o', 'p', 's', 't']
  97: >>> sorted(word1) == sorted(word2)
True
  98: >>> word3 = 'stops'
  99: >>> sorted(word1) == sorted(word3)
False
 100:
>>> d = {}
... for word in [word1, word2, word3]:
...     signature = sorted(word) 
...     print(signature)
...
 101:
>>> d = {}
... for word in [word1, word2, word3]:
...     signature = tuple(sorted(word)) 
...     print(signature)
...
 102:
>>> d = {}
... for word in [word1, word2, word3]:
...     signature = tuple(sorted(word)) 
...     print(signature)
...     d[signature]
...
 103:
>>> d = {'opts': ['stop', 'pots'], 
... 'ab': ['ab', 'ba'],
... 'a': ['a']}
...
 104:
>>> for v in d.values():
...     if len(v) > 1:
...         print(v)
...