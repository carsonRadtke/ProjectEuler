def sum_of_fifth_powers(n):
    return sum(map(lambda n: int(n)**5, str(n)))
    
def main():
    total = 0
    for val in range(10, 354295):
        if (sum_of_fifth_powers(val) == val):
            total += val

    print(total)

if __name__ == "__main__":
    main()

