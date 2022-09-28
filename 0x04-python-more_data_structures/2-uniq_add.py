#!/usr/bin/python3

def uniq_add(my_list=[]):
	"""
	adds all unique integers in a list
	Args:
		my_list - given list
	Return:
		Data - sum
	"""

	x = list(set(my_list))
	return sum(x)
