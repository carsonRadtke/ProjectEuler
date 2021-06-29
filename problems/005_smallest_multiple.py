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

def factors(num):

    factors = {}

    primes_below_num = prime_generator(num)

    for x in primes_below_num:
        powers = 0
        while num % x == 0:
            powers += 1
            num /= x
        if powers > 0:
            factors[x] = powers

    return factors

def main():
    factor_dicts = [factors(x+1) for x in range(20)]
    prime_factorization = [0 for _ in range(len(factor_dicts))]

    for factor_dict in factor_dicts:
        for prime, power in factor_dict.items():
            prime_factorization[prime-1] = max(prime_factorization[prime-1], power)

    smallest_multiple = 1

    for idx in range(len(prime_factorization)):
        smallest_multiple *= pow(idx+1, prime_factorization[idx])

    print(smallest_multiple)

if __name__ == "__main__":
    main()