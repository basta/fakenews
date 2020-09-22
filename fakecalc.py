import analysis

truedata = {}
fakedata = {}

#Load data
for line in open("data/fakeratios.txt").readlines():
    line = line.split()
    fakedata[line[0]] = float(line[1])

for line in open("data/trueratios.txt").readlines():
    line = line.split()
    truedata[line[0]] = float(line[1])

def fakecalc(text):
    text = analysis.cleanup(text)
    trueval = 0
    fakeval = 0
    for word in text.split():
        if word in truedata:
            trueval += truedata[word]
        if word in fakedata:
            fakeval += fakedata[word]

    return trueval / (fakeval + trueval)

if __name__ == "__main__":
    text = " ".join(open("text.txt").readlines())
    print("Truthness:", fakecalc(text))
    