#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
# ADD YOUR CODE HERE
def print_reversed_list(list):
	length = len(list)
	i = length - 1
	while i >= 0:
		print(list[i])
		i-= 1

print_reversed_list(list_)

# Pythonic version of for loop in reverse
def print_reversed_list_p(list):
	length = len(list)
	for i in range(length-1, -1, -1):
		print(list[i])

