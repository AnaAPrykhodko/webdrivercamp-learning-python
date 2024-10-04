#!/usr/bin/python3
string = """AbraCadabra
A new string voila!"""
def remove_char(some_string):
  # ADD YOUR CODE HERE
	new_string = """"""
	for char in some_string:
		if char != 'a' and char != 'A':
			new_string += char
	return new_string

print(remove_char(string))	
