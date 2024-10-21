#!/usr/bin/python3
def common_elements(a, b):
    # YOUR CODE HERE
	common_set = set()
	for element in a:
		if element in b:
			common_set.add(element)
	return common_set


if __name__=="__main__":
    set_a = { "API", "requests", "Selenium", "Python", "Behave"}
    set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
