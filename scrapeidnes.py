import urllib.request
from bs4 import BeautifulSoup
import progressbar


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
f = open("idnes.txt", "w+")
for i in progressbar.progressbar(range(1, 2000)):
    url = "http://www.idnes.cz/zpravy/archiv/%i" % (i)
    print(url)
    request=urllib.request.Request(url,None,headers) #The assembled request
    try:
        response = urllib.request.urlopen(request)
    except:
        continue
    data = response.read()
    soup = BeautifulSoup(data, "lxml")
    counter = 1
    for link in soup.find_all("a", {"class": "art-link"}):
        content = "\nSTART OF ARTICLE %i - %i\n" % (i, counter)
        counter +=1
        link = link.get("href")
        try:
            request=urllib.request.Request(link,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
        except Exception as e:
            print(e)
            continue 
        data = response.read()
        soup = BeautifulSoup(data, "lxml")
        #print(soup.prettify())
        try:
            div = soup.find("div", id="art-text")
            for par in div.find_all("p"):
                content += par.text
            f.write(content)
            f.write(" ")
        except AttributeError:
            continue

    f.write(content)