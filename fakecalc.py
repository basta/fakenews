import analysis
from bs4 import BeautifulSoup
import urllib

def fakecalc(text):
    text = analysis.cleanup(text)
    trueval = 0
    fakeval = 0
    for word in text.split():
        if word in truedata:
            trueval += truedata[word]
        if word in fakedata:
            fakeval += fakedata[word]
    try:
        return trueval / (fakeval + trueval)
    except ZeroDivisionError:
        return 0
        
def text_from_html(html):
    soup = BeautifulSoup(html)
    paragraphs = soup.find_all("p")
    result = " ".join([i.text for i in paragraphs])
    return result

def url_to_html(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    try:
        response = urllib.request.urlopen(request)
    except:
        return ""
    return response.read()

truedata = {}
fakedata = {}

#Load data
for line in open("data/fakeratios.txt").readlines():
    line = line.split()
    fakedata[line[0]] = float(line[1])

for line in open("data/trueratios.txt").readlines():
    line = line.split()
    truedata[line[0]] = float(line[1])


if __name__ == "__main__":
    text = " ".join(open("text.txt").readlines())
    print("Truthness:", fakecalc(text))
    