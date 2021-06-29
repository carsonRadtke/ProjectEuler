def main():
	nats_below_1k = [x for x in range(1, 1000)]
	multiples_of_3_or_5 = filter(lambda x: (x % 5) * (x % 3) == 0, nats_below_1k)
	sum_of_multiples = sum(multiples_of_3_or_5)

	print(sum_of_multiples)

if __name__ == "__main__":
	main()
