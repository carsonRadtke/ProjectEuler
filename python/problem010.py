from math import sqrt

def isPrime(n):
    if (n == 2):
        return True
    for x in range(2, int(sqrt(n))+1):
        if (n % x == 0):
            return False
    return True

def main():
    output = 0
    for x in range(2, 2000000):
        if (isPrime(x)):
            output = output + x
    print(output)

main()