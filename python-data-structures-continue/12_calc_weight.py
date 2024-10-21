#!/usr/bin/python3
def calc_weight(list_=[]):
  # YOUR CODE HERE
	if list_ == []:
		return 0
	else:
		length = len(list_)
		mult_sum = 0
		div_sum = 0
		for i in range(length):
			mult_sum += list_[i][0] * list_[i][1]
			div_sum += list_[i][1]
		return mult_sum / div_sum


if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
