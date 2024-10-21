#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
  # YOUR CODE GOES HERE
	lst = [0] * list_len
	try:
		for i in range(list_len):
			try:
				lst[i] = list_1[i] / list_2[i]
			except ZeroDivisionError:
				print("division by 0")
			except TypeError:
				print("wrong type")
			except IndexError:
				print("out of range")
	finally:
		return lst
	

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
