def factorial(num):
    ret = 1
    for i in range(num):
        ret *= i+1
    return ret

def main():
    factorial_digits = str(factorial(100))
    factorial_digit_sum = sum(map(int, factorial_digits))

    print(factorial_digit_sum)

if __name__ == "__main__":
    main()