def main():
    sum_of_squares = sum([(x+1)**2 for x in range(100)])
    square_of_sums = sum([x+1 for x in range(100)])**2
    sum_square_difference = square_of_sums - sum_of_squares

    print(sum_square_difference)

if __name__ == "__main__":
    main()