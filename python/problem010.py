from math import sqrt, ceil

def isPrime(n):
    sq = sqrt(n)
    bound = ceil(sq)+1
    for x in range(2, bound):
        if (n % x == 0):
            return False
    return True

def main():
    output = 2 + 3
    for x in range(5, 2000000, 6):
        if (isPrime(x)):
            output = output + x
        if (isPrime(x+2)):
            output = output + x + 2
    print(output)

main()