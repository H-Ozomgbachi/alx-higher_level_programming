#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
	x = list(set(my_list))
	return reduce(lambda p,q: p + q, x)
