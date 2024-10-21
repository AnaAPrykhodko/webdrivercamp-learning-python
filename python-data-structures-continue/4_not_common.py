#!/usr/bin/python3
def not_common_elements(a, b):
    # YOUR CODE HERE
	not_common_set = set()
	for element in a:
		if element not in b:
			not_common_set.add(element)
	for element in b:
		if element not in a:
			not_common_set.add(element)
	return not_common_set


if __name__=="__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
