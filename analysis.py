what = "idnes"

if what == "idnes":
    f = open("idnes.txt")
    o = open("idnesfreq.txt", "w+")
elif what == "bpk":
    f = open("bpk.txt")
    o = open("bpkfreq.txt", "w+")

words = {}

def cleanup(s: str):
    s = s.lower()
    s = s.replace(",", "")
    s = s.replace(".", "")
    s = s.replace("\"", "")
    s = s.replace(":", "")
    s = s.replace("”", "")
    s = s.replace("„", "")
    s = s.replace("?", "")
    s = s.replace("!", "")
    s = s.replace("–", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    return s

if __name__ == "__main__":
    while True:
        line = f.readline()
        if line == "":
            break
        if "START OF ARTICLE" in line:
            print(line.split()[3])
            continue
        for word in line.split():
            word = cleanup(word)
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        
        
    print(len(words.items()))
    sorted_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
    for word in sorted_words:
        o.write("%s %i\n" % (word, sorted_words[word]))

    print("Total: ", sum(sorted_words.values()))
