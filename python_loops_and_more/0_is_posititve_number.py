#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
#ADD YOUR CODE HERE
if random_num < 0:
	print(f"{random_num} is negative")
elif random_num > 0:
	print(f"{random_num} is positive")
else:
	print(f"{random_num} is zero")

