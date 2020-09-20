import matplotlib
bpk_total = 3069208
idnes_total = 30734788

f1 = open("bpkfreq.txt")
f2 = open("idnesfreq.txt")

f1data = {}
f2data = {} 

for line in f1.readlines():
    try:
        line = line.split()
        f1data[line[0]] = int(line[1])
    except:
        print(line)

for line in f2.readlines():
    try:
        line = line.split()
        f2data[line[0]] = int(line[1])
    except:
        print(line)

ratios1 = {}
ratios2 = {}
for key in f1data:
    if key in f2data:
        val = f1data[key] * (idnes_total/bpk_total) / f2data[key]
        if val < 1:
            ratios1[key] = 1/val
        
        if val >= 1:
            ratios2[key] = val

sorted_ratios1 = {k: v for k, v in sorted(ratios1.items(), key=lambda item: item[1])}
sorted_ratios2 = {k: v for k, v in sorted(ratios2.items(), key=lambda item: item[1])}

o1 = open("idnesratios.txt", "w+")
o2 = open("bpkratios.txt", "w+")

for key in sorted_ratios1:
    o1.write("%s %f\n" % (key, sorted_ratios1[key]))

for key in sorted_ratios2:
    o2.write("%s %f\n" % (key, sorted_ratios2[key]))