def main():

    distinct_powers = dict()

    for a in range(2, 101):
        for b in range(2, 101):
            distinct_powers[a**b] = True

    print(len(distinct_powers.keys()))

if __name__ == "__main__":
    main()