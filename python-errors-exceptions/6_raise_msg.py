#!/usr/bin/python3
def raise_message(message=""):
  # YOUR CODE GOES HERE
	raise NameError(message)


if __name__ == "__main__":
    try:
        raise_message("I love Python!")
    except NameError as ne:
        print(ne)
