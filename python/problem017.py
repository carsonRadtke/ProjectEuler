
def numberToString(n):
	if (n == 0):
		return ""
	if (n < 10):
		return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][n-1]
	if (n < 20):
		return ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n-10]
	if (n < 30):
		return "twenty" + numberToString(n-20)
	if (n < 40):
		return "thirty" + numberToString(n-30)
	if (n < 50):
		return "forty" + numberToString(n-40)
	if (n < 60):
		return "fifty" + numberToString(n-50)
	if (n < 70):
		return "sixty" + numberToString(n-60)
	if (n < 80):
		return "seventy" + numberToString(n-70)
	if (n < 90):
		return "eighty" + numberToString(n-80)
	if (n < 100):
		return "ninety" + numberToString(n-90)
	if (n < 200):
		if (n == 100):
			return "onehundred"
		return "onehundredand" + numberToString(n-100)
	if (n < 300):
		if (n == 200):
			return "twohundred"
		return "twohundredand" + numberToString(n-200)
	if (n < 400):
		if (n == 300):
			return "threehundred"
		return "threehundredand" + numberToString(n-300)
	if (n < 500):
		if (n == 400):
			return "fourhundred"
		return "fourhundredand" + numberToString(n-400)
	if (n < 600):
		if (n == 500):
			return "fivehundred"
		return "fivehundredand" + numberToString(n-500)
	if (n < 700):
		if (n == 600):
			return "sixhundred"
		return "sixhundredand" + numberToString(n-600)
	if (n < 800):
		if (n == 700):
			return "sevenhundred"
		return "sevenhundredand" + numberToString(n-700)
	if (n < 900):
		if (n == 800):
			return "eighthundred"
		return "eighthundredand" + numberToString(n-800)
	if (n < 1000):
		if (n == 900):
			return "ninehundred"
		return "ninehundredand" + numberToString(n-900)
	if (n == 1000):
		return "onethousand"

def main():
	total = 0
	for x in range(1, 1001):
		total = total + len(numberToString(x))
	print(total)

main()
