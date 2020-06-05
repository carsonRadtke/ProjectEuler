def fib(n):
    def _fib(n, l):
        if (n >= len(l)):
            l.insert(n, _fib(n-1, l)+_fib(n-2, l))
        return l[n]
    return _fib(n, list((1, 1)))

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