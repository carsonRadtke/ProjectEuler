def fact(n):
    def _fact(i, s):
        if (i <= 1):
            return s
        return _fact(i-1, s*i)
    return _fact(n, 1)

def main():
    out = 0
    for x in str(fact(100)):
        out = out + int(x)
    print(out)

main()
