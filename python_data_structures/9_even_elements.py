#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
# ADD YOUR CODE HERE
the_list = []
for item in my_list:
	if item % 2 == 0:
		the_list.append(True)
	else:
		the_list.append(False)

the_tuple = tuple(the_list)
print(my_list)
print(the_tuple)
