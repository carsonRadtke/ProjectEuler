from math import sqrt

def isPrime(n):
    if (n == 2):
        return True
    for x in range(2, int(sqrt(n))+1):
        if (n % x == 0):
            return False
    return True

def main():
    count = 1
    num = 1

    while (count < 10001):
        num = num + 2
        if (isPrime(num)):
            count = count + 1
        
    print(num)

main()