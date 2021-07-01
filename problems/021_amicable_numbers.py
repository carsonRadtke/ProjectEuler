from math import sqrt, ceil

def proper_divisors(n):
    ret = []
    if n <= 1:
        return [0]
    for x in range(1, ceil(sqrt(n))):
        if n % x == 0:
            ret.append(x)
            if (x * x != n) and x > 1:
                ret.append(n / x)
    return ret

def d(n):
    return sum(proper_divisors(n))

def is_amicable(num):
    return d(num) != num and d(d(num)) == num

def main():
    amicable_numbers = filter(is_amicable, range(2, 10000))
    amicable_numbers_sum = sum(amicable_numbers)

    print(amicable_numbers_sum)

if __name__ == "__main__":
    main()