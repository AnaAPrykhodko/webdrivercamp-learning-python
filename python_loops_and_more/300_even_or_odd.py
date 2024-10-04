#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)


def get_status(n):
	if n % 2 == 0:
		return "even"
	else:
		return "odd"


last = abs(random_num) % 10
if last == 0:
	print(f"{random_num} - the last digit {last} is zero")
else:
	status = get_status(last)
	if random_num < 0:
		print(f"{random_num} - the last digit -{last} is {status}")
	else:
		print(f"{random_num} - the last digit {last} is {status}")
