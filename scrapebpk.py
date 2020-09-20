import urllib.request
from bs4 import BeautifulSoup
import progressbar


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
f = open("bpk.txt", "w+")
for i in progressbar.progressbar(range(95762, 1, -1)):
    url = "http://www.bezpolitickekorektnosti.cz/?p=%i" % (i)
    print(url)
    request=urllib.request.Request(url,None,headers) #The assembled request
    try:
        response = urllib.request.urlopen(request)
    except:
        continue
    data = response.read()
    soup = BeautifulSoup(data, "lxml")
    content = "\nSTART OF ARTICLE %i\n" % i
    for prg in soup.find("div", {"class": "entry-content"}).find_all("p"):
            content+=(prg.get_text())
            content+= " "          
    f.write(content)