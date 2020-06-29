from functools import cmp_to_key


def cmp(a, b):
	a = a.split('.')
	b = b.split('.')
	i = 0 ;
	while i < min(len(a), len(b)):
		z = int(a[i]) - int(b[i])
		i = i + 1 
		if z == 0:
			continue
		if z < 0:
			return -100
		else:
			return 100


	if len(a) < len(b):
		return -100
	return 100



def solution(l):
	r = sorted(l, key=cmp_to_key(cmp))
	res = ','.join(r)
	print(res)
