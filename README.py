# A.-Restoring-Three-Numbers
x1, x2, x3, x4 = map(int, input().split())
_max = max(x1, x2, x3, x4)
lst = []
if x1 != _max:
	s = _max - x1
	lst.append(s)
if x2 != _max:
	p = _max - x2
	lst.append(p)
if x3 != _max:
	d = _max - x3
	lst.append(d)
if x4 != _max:
	f = _max - x4
	lst.append(f)
print(*lst)
