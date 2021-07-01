def fibonacci_generator(cb):
    yield 1
    a, b, term = 0, 1, 2
    val = a + b
    while cb(term)(val):
        yield val
        a, b = b, val
        val, term = a + b, term + 1

def main():
    fib_numbers = [fib_num for fib_num in fibonacci_generator(lambda _: lambda val: len(str(val)) < 1000)]
    _1000_digit_fibonacci_number = len(fib_numbers)+1

    print(_1000_digit_fibonacci_number)

if __name__ == "__main__":
    main()