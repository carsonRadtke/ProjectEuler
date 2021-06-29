def is_palindrome(s):
    return str(s) == str(s)[::-1]

def main():
    products_of_3dns = [str(x*y) for x in range(y, 100) for y in range(10, 100)]
    palindromes_of_3dns = filter(is_palindrome, products_of_3dns)
    largest_palindrome_product = max(palindromes_of_3dns)

    print(largest_palindrome_product)

if __name__ == "__main__":
    main()