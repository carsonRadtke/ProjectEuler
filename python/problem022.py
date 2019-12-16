file_name = "./assets/p022_names.txt"

def namesToArray():
	return open(file_name).read().replace('"', '').split(",")

def score(s):
	if (len(s) == 1):
		return ord(s[0])-ord('A')+1
	return (ord(s[0]) - ord('A') + 1) + score(s[1:])

def main():
	out = 0
	arr = sorted(namesToArray())
	for x in range(0, len(arr)):
		out = out + score(arr[x])*(x+1)
	print(out)

main()
