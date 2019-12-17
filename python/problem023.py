from math import sqrt

def isAbundant(n):
    tot = 0
    for x in range(2, int(sqrt(n))+1):
        if (n % x == 0):
            tot = tot + x + n/x
        if (x * x == n):
            tot = tot - x
    return tot > n

def main():
    # TODO
    return None    

main()



