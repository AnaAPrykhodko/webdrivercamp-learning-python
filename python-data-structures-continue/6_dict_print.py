#!/usr/bin/python3
def dict_print(dict_):
    # YOUR CODE HERE
	for item in sorted(dict_):
		print(f"{item}: {dict_[item]}")	


if __name__=="__main__":
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)
