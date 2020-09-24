from googlesearch import search
from fakecalc import *
from bs4 import BeautifulSoup

def is_independent(soup, from_sites):
    links = soup.find_all("a")
    for link in links:
        try:
            link = link["href"]
            for site in from_sites:
                if site in link:
                    return False
        except KeyError:
            continue

    return True


def truthness_from_url(url, independence_check=False):
    if type(independence_check) == list:
        html = url_to_html(url)
        soup = BeautifulSoup(html, "lxml")
        if not is_independent(soup, independence_check):
            return 0

    return fakecalc(text_from_html(url_to_html(url)))


def statement_truth(stat, literal=False, source=None):
    results = []
    link_truth = [] #List of [[Site, Truth Value]]
    read_sites = [] #List of sites that were already analyzed so we dont use one source multiple times
    if source is not None:
        read_sites.append(source) #Dont analyze readers source

    n_results = 0
    if literal:
        stat = "\"" + stat
        stat += "\""

    for link in search(stat,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'cz',  # The language
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = None,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                ):
        
        if len(read_sites) > 0:
            for site in read_sites:
                if site in link:
                    continue

            truthness = truthness_from_url(link, read_sites)
            if truthness != 0 and truthness != 1:
                link_truth.append([link, truthness])
                read_sites.append(link.split("/")[2])
                print("independent", link, read_sites)
            else:
                continue

        else:
            truthness = truthness_from_url(link)
            link_truth.append(link, truthness)
        
        n_results += 1
        results.append(link)
        if n_results == 5:
            pass
            break

    if len(results) == 0:
        print("Nenalezeny žádné výslekdy")
        return 0
    
    if len(results) == 1:
        print("Nalezen pouze jeden výsledek")
        return 0

    print("\n")
    print("-"*32, "RESULTS", "-"*32)
    suma = 0
    amount_of_results = 0
    
    for link, truth in link_truth:
        #link = link_truth[0]
        #truth = link_truth[1]
        amount_of_results += 1
        print(truth, link)
        suma += truth


    print("\nTotal:", suma/amount_of_results)
    
statement_truth("Češi na poslední chvíli nakupovali v Německu zásoby", literal=True, source="www.novinky.cz")
#print(statement_truth("Zeman je idiot"))