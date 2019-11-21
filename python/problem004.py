def isPalin(s):
    return s == s[::-1]

def main():
    output = 0

    for x in range(100,1000):
        for y in range(100,1000):
            num = x*y
            if (isPalin(str(num))):
                output = max(output, num)
    
    print(output)

main()
                