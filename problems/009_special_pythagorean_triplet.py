def main():

    special_pythagorean_triplet = None

    for a in range(1, 1000):
        if special_pythagorean_triplet is not None:
            break
        for b in range(a, 1000):
            c = 1000 - (a + b)
            if (a**2+b**2==c**2):
                special_pythagorean_triplet = (a, b , c)
                break

    (a,b,c) = special_pythagorean_triplet
    print (a*b*c)
                

if __name__ == "__main__":
    main()