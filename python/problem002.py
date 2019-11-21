def fib(n):
    if (n <= 2):
        return 1
    return fib(n-1) + fib(n-2)

def main():
    output = 0

    term = 1
    value = fib(term)

    while (value <= 4000000):
        if (value % 2 == 0):
            output = output + value
        term = term + 1
        value = fib(term)

    print(output)

main()