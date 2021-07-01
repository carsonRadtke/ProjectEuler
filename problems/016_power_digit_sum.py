def sum_of_digits(n):
    return sum(map(int, str(n)))

def main():
    power_digit_sum = sum_of_digits(2**1000)

    print(power_digit_sum)

if __name__ == "__main__":
    main()