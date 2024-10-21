#!/usr/bin/python3
def only_unique(list_=[]):
    # YOUR CODE HERE
	unique_list = []
	for n in list_:
		if n not in unique_list:
			unique_list.append(n)
	return sum(unique_list)


if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
