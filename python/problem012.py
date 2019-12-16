from math import sqrt

def triangle():
	ret = 0
	delta = 1
	while (1):
		ret = ret + delta
		yield (ret)
		delta = delta + 1

def divisors(n):
	ret = 1
	for x in range(1, int(sqrt(n))):
		if (n % x == 0):
			ret = ret + 2
		if (x * x == n):
			ret = ret - 1
	return ret


def main():
	t_g = triangle()
	found = False
	while (not found):
		t = t_g.next()
		if (divisors(t) > 500):
			print(t)
			break

main()
