def main():
    output = 0
    for a in range(0,1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if (a + b + c > 1000):
                    break
                if (a + b + c == 1000):
                    if (a*a+b*b==c*c):
                        output = a*b*c
                        break
    print(output)

main()