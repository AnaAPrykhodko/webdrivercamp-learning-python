#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
# ADD YOUR CODE HERE

def replace_element(list, index, element):
	length = len(list)
	if index < 0 or index >= length:
		print(list)
	else:
		list[index] = element
		print(list)

replace_element(list_, index, element_to_replace)
