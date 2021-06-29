def fibonacci_generator(stop):

	penultimate, ultimate = 0, 1

	while ultimate < stop:

		yield (next := penultimate + ultimate)

		penultimate, ultimate = ultimate, next
		

def main():
	fibonacci_numbers = [x for x in fibonacci_generator(4000000)]
	even_fibonacci_numbers = filter(lambda x: x % 2 == 0, fibonacci_numbers)
	sum_of_evens = sum(even_fibonacci_numbers)

	print(sum_of_evens)


if __name__ == "__main__":
	main()
