from math import sqrt, ceil

def triangle_number_generator():
    nat, ret = 1, 0

    while True:
        ret += nat
        yield ret
        nat += 1

def factors(n):
    ret = []

    for x in range(1, ceil(sqrt(n))):
        if n % x == 0:
            ret.append(x)
            if x * x != n:
                ret.append(n / x)

    return ret

def main():
    highly_divisible_triangular_number = None

    for x in triangle_number_generator():
        if (len(factors(x)) > 500):
            highly_divisible_triangular_number = x
            break

    print(highly_divisible_triangular_number)

if __name__ == "__main__":
    main()