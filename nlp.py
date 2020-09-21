import nltk

print("Reading data...")
tokens = open("isenttok.txt").readlines()
text = nltk.Text(tokens)

print("Finished")

print("Calculating...")
print(text.concordance("a"))
print("done")