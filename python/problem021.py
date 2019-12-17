from math import sqrt

def d(n):
    ret = 1
    for x in range(2, int(sqrt(n))):
        if (n % x == 0):
            ret = ret + x + n/x
        if (x*x == n):            
            ret = ret - x
    return ret

def main(): 
    out = 0
    for x in range(0, 10000):
        if (d(x) != x and d(d(x)) == x):
            out = out + x
    print(out)

main()
