#!/usr/bin/python3
def divide_safe(a, b):
  # YOUR CODE GOES HERE
	c = None
	try: 
		c = a / b
	except ZeroDivisionError:
		pass
	finally:
		print(f"Result: {c}")
	return c


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
