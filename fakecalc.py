import analysis

text = " ".join(open("text.txt").readlines())

truedata = {}
fakedata = {}

#Load data
for line in open("bpkratios.txt").readlines():
    line = line.split() 
    fakedata[line[0]] = float(line[1])

for line in open("idnesratios.txt").readlines():
    line = line.split() 
    truedata[line[0]] = float(line[1])

text = analysis.cleanup(text)

trueval = 0
fakeval = 0
for word in text.split():
    if word in truedata:
        trueval += truedata[word]
    if word in fakedata:
        fakeval += fakedata[word]

print("Trueval: ", trueval)
print("Fakeval: ", fakeval)
