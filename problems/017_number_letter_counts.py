zero_to_nine = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
twenty_to_hundred = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def word_form(num):
    if (num >= 1000):
        div = int(num / 1000)
        mod = num % 1000
        return word_form(div) + "thousand" + ("and" if (0 < mod < 100) else "") + word_form(mod)
    if (num >= 100):
        div = int(num / 100)
        mod = num % 100
        return word_form(div) + "hundred" + ("and" if (0 < mod < 100) else "") + word_form(mod)
    if (num >= 20):
        return twenty_to_hundred[int(num/10)-2] + word_form(num % 10)
    if (num >= 10):
        return ten_to_nineteen[num - 10]
    return zero_to_nine[num]

def main():
    number_letter_counts = 0
    for i in range(1000):
        number_letter_counts += len(word_form(i+1))

    print(number_letter_counts)

if __name__ == "__main__":
    main()