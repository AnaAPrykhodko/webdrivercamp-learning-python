#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2
# ADD YOUR CODE HERE
def get_element(list, index):
	length = len(list)
	if index < 0 or index >= length:
		return None
	else:
		print(f"The element retrieved is {list[index]}")

get_element(list_, index)
