#!/usr/bin/python3

import sys

arguments_list = sys.argv
length = len(arguments_list)
if length == 1:
	print("0 arguments.")
elif length == 2:
	print("1 argument:")
	print(f"1: {arguments_list[1]}")
else:
	print(f"{length-1} arguments:")	
	for argument in arguments_list[1:]:
		index = arguments_list.index(argument)
		print(f"{index}: {argument}")
