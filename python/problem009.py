def main():
    output = 0
    for a in range(0,1000):
        for b in range(a, 1000-a):
            c = 1000-(a+b)
            if (a*a+b*b==c*c):
                output = a*b*c
                break
    print(output)

main()