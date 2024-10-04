#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# ADD YOUR CODE HERE
def print_matrix(some_matrix):
	for row in matrix:
		for item in row:
			print(item, end=" ")
		print()



print_matrix(matrix)
	
