def main():
    output = 0
    for x in range(0, 1000):
        if (x % 5 == 0 or x % 3 == 0):
            output = output + x
    print(output)

main()