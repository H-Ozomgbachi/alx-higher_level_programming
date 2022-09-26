#!/usr/bin/python3
def element_at(my_list, idx):
	if idx < 0:
		return None
	try:
		return my_list[idx]
	except:
		return None
