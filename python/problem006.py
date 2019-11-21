def main():
    output = 0

    sumOfSquares = 0
    squareOfSums = 0

    for x in range(0,101):
        sumOfSquares = sumOfSquares + x*x
        squareOfSums = squareOfSums + x
    
    output = squareOfSums*squareOfSums - sumOfSquares

    print(output)

main()