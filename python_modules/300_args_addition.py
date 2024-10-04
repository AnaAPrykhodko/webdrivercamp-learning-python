#!/usr/bin/python3
import sys

sum = 0
for argument in sys.argv[1:]:
	sum += int(argument)
print(sum)
	
