#!/usr/bin/python3
def tuple_addition(first_arg=(), second_arg=()):
	if len(first_arg) == 0 and len(second_arg) == 0:
		first_num = 0
		second_num = 0
	elif len(first_arg) == 1 and len(second_arg) == 0:
		first_num = first_arg[0]
		second_num = 0
	elif len(first_arg) == 0 and len(second_arg) == 1:
                first_num = 0
                second_num = second_arg[0]
	elif len(first_arg) == 1 and len(second_arg) == 1:
		first_num = first_arg[0] + second_arg[0]
		second_num = 0
	elif len(first_arg) == 1 and len(second_arg) > 1:
		first_num = first_arg[0] + second_arg[0]
		second_num = second_arg[1]
	elif len(first_arg) > 1 and len(second_arg) == 1:
		first_num = first_arg[0] + second_arg[0]
		second_num = first_arg[1]
	elif len(first_arg) == 0 and len(second_arg) > 1:
		first_num = second_arg[0]
		second_num = second_arg[1]
	elif len(first_arg) > 1 and len(second_arg) == 0:
		first_num = first_arg[0]
		second_num = first_arg[1]
	else:
		first_num = first_arg[0] + second_arg[0]
		second_num = first_arg[1] + second_arg[1]
	return first_num, second_num


