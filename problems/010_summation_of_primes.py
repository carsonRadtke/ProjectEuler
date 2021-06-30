from math import sqrt, ceil

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    for x in range(3, ceil(sqrt(num))+1):
        if num % x == 0:
            return False

    return True

def prime_generator(cap):
    yield 2

    current_prime = 3

    while current_prime <= cap:
        yield current_prime
        
        current_prime += 2

        while not is_prime(current_prime):
            current_prime += 2

def main():
    summation_of_primes = sum([x for x in prime_generator(2000000)])

    print(summation_of_primes)

if __name__ == "__main__":
    main()