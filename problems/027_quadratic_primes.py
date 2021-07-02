from math import ceil, sqrt


def is_prime(num):
    if (num <= 0):
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    for x in range(3, ceil(sqrt(num))+1):
        if num % x == 0:
            return False

    return True


def quadratic_generator(a, b):

    def f(n):
        return n**2 + a * n + b

    val = f(term := 0)
    while is_prime(val):
        yield val
        val = f(term := term + 1)

def main():
    best_product, best_length = -1, -1
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            generated_primes = [prime for prime in quadratic_generator(a, b)]
            if (len(generated_primes) > best_length):
                best_product = a * b
                best_length = len(generated_primes)
    
    print(best_product)

if __name__ == "__main__":
    main()