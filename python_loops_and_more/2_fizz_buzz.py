#!/usr/bin/python3
def fizz_buzz():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz ", end="")
		else:
			if i % 3 == 0:
				print("Fizz ", end="")
			elif i % 5 == 0:
				print("Buzz ", end="")
			else:
				print(i, " ", end="")	
	

fizz_buzz()

