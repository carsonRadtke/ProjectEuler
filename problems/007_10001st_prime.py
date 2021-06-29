from math import sqrt, ceil

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    for x in range(3, ceil(sqrt(num)+1)):
        if num % x == 0:
            return False

    return True

def prime_generator(count):
    if (count < 1):
        return []

    yield 2

    current_prime = 3
    counter = 1

    while counter < count:
        yield current_prime
        
        current_prime += 2
        counter += 1

        while not is_prime(current_prime):
            current_prime += 2

def main():
    first_10001_primes = [prime for prime in prime_generator(10001)]
    _10001st_prime = first_10001_primes[10000]
    
    print(_10001st_prime)

if __name__ == "__main__":
    main()