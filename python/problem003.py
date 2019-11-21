def main():
    num = 600851475143 
    fact = 1

    while (num >= fact):
        fact = fact + 1
        while (num % fact == 0):
            num = num / fact

    print(fact)

main()