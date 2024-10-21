#!/usr/bin/python3
def compute_matrix(matrix=[]):
	new_matrix = []
	for row in matrix:
		new_row = []
		for n in row:
			new_row.append(n**2)
		new_matrix.append(new_row)
	return new_matrix


if __name__=="__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
