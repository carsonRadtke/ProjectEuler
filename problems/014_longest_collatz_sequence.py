def collatz_generator(cb):

    def collatz(n, lut):
        if n in lut.keys():
            return lut[n]
        
        lut[n] = 1 + collatz(int(n/2) if (n % 2 == 0) else int(3 * n + 1), lut)
        return lut[n]

    term, lut = 1, {1: 1}
    while cb(term)(val := collatz(term, lut)):
        yield val
        term = term + 1

def main():
    collatz_sequences = [x for x in collatz_generator(lambda term: lambda val: term < 1000000)]
    longest_collatz_sequence_val = max(collatz_sequences)
    longest_collatz_sequence = collatz_sequences.index(longest_collatz_sequence_val) + 1

    print(longest_collatz_sequence)

if __name__ == "__main__":
    main()