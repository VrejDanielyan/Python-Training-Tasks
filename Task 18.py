# 18. Implement function which will take number and return sum of digits in number


def sum_of_digits(n):
	if n == 0:
		return 0
	return (n % 10 + sum_of_digits(n//10))

print(sum_of_digits(134545))
