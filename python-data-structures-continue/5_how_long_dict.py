#!/usr/bin/python3
def keys_number(d):
    # YOUR CODE HERE
	n = 0
	for key in d:
		n += 1
	return n


if __name__=="__main__":
    dict_ = {"lib": "requests", 1: "Selenium", "lang": "Python", "frame": "Behave"}
    number_of_keys = keys_number(dict_)
    print(f"The dictionary has {number_of_keys} keys")
