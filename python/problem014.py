def collatz(n):
	def _collatz(i, c):
		if (i == 1):
			return c+1
		if (i & 1):
			return _collatz(3*i+1, c+1)
		return _collatz(i//2, c+1)
	return _collatz(n, 0)

def main():
	start = 1
	chain = 1
	for x in range(1, 1000000):
		ch = collatz(x)
		if (ch > chain):
			start = x
			chain = ch
	print (start)

main()
