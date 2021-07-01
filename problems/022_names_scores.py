names_file = "/Users/carson/code/ProjectEuler/assets/p022_names.txt"
names_file_contents = open(names_file).readline()
(names_text := list(map(lambda x: x.replace("\"", ""), names_file_contents.split(",")))).sort()

def name_score(name):
    ret = 0
    for x in name:
        ret += ord(x) - ord("A") + 1
    return ret

def main():
    names_zip = zip(names_text, range(1, len(names_text)+1))
    names_scores = sum(map(lambda x: name_score(x[0])*x[1], names_zip))

    print(names_scores)

if __name__ == "__main__":
    main()