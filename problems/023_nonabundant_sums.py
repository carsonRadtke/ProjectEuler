def divisors(n):
    ret = []
    if n <= 1:
        return [0]
    for x in range(n):
        val = x + 1
        if (val * val > n):
            break
        if n % val == 0:
            ret.append(val)
            if (val * val != n):
                ret.append (int(n/val))
    return ret

def is_abundant(num):
    return sum(divisors(num)) > 2*num

def abundant_number_generator(cb):

    term, val = 1, 12
    while cb(term)(val):
        yield val

        term, val = term + 1, val + 1
        while not is_abundant(val):
            val += 1


def main():

    (abundant_numbers := [num for num in abundant_number_generator(lambda _: lambda val: val < 28123)]).sort()
    abundant_numbers_dict = dict((num, True) for num in abundant_numbers)

    def is_nonabundant_sum(num):
        for y in abundant_numbers:
            if abundant_numbers_dict.get(num - y, False):
                return False
        return True

    nonabundant_sums = sum(filter(is_nonabundant_sum, range(28123)))

    print(nonabundant_sums)


if __name__ == "__main__":
    main()
