from math import sqrt

def corners(n):
    if (n == 1):
        return (1, 1, 1, 1)
    ul, ur, bl, br = corners(n - 2)
    ur = int(sqrt(ur)+2)**2
    ul = ur - n + 1
    bl = ul - n + 1
    br = bl - n + 1
    return ((ul), ur, bl, br)

def main():
    total = 1
    for x in range(3, 1002, 2):
        total += sum(corners(x))

    print(total)

if __name__ == "__main__":
    main()