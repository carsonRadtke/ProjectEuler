def flatten(list_of_lsts):
    ret = []
    for lst in list_of_lsts:
        for item in lst:
            ret.append(item)
    return ret

def combine(letter, perms):
    return map(lambda perm: str(letter) + str(perm), perms)

def permutations(string):
    if len(string) == 1:
        return string
    return flatten(map(lambda letter: combine(str(letter), permutations(string.replace(letter, ""))), string))

def main():
    print(permutations("0123456789")[999999])

if __name__ == "__main__":
    main()