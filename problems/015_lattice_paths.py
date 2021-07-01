def lattice_paths(w, h, lut = [[None for _ in range(20)] for _ in range(20)]):
    if lut[h-1][w-1] is not None:
        return lut[h-1][w-1]

    if h == 1:
        lut[h-1][w-1] = w+1
    elif w == 1:
        lut[h-1][w-1] = h+1
    else:
        lut[h-1][w-1] = lattice_paths(w-1, h, lut) + lattice_paths(w, h-1, lut)

    return lut[h-1][w-1]

def main():
    print(lattice_paths(20, 20))

if __name__ == "__main__":
    main()