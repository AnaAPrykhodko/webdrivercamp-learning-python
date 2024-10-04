#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
# ADD YOUR CODE HERE

def replace_element(list_original, index, element):
	list_copy = list(list_original)
	length = len(list_original)
	if index < 0 or index >= length:
		print(f"Copy: {list_copy}\nOriginal: {list_original}")
	else:
		list_copy[index] = element
		print(f"Copy: {list_copy}\nOriginal: {list_original}")

replace_element(list_, index, element_to_replace)
