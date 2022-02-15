import requests
import networkx as nx

from bs4 import BeautifulSoup
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

fix = "https://en.wikipedia.org" 
url = "https://en.wikipedia.org/wiki/Delhi"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

a_tags = soup.find_all("a", href=True)
links = []
extra_links = []

for link in a_tags:
    if link.text:
        if(link["href"][0]!='#'):{
            links.append(link["href"])
        }

cleaned_links = list(set(links))

for link in cleaned_links:
    if(link[0]=='h'):
        extra_links.append(link)
        cleaned_links.remove(link)

def_urls = []
page_details = []

for link in cleaned_links:
    if(link[0:6] == "/wiki/"):
        url_temp = fix + link
        def_urls.append(url_temp)
    else:
        extra_links.append(link)
        cleaned_links.remove(link)

# for url in def_urls:
#     print(url)

# print(len(def_urls))
################  For Extracting the text for the cleaned wikipedia links but the time complexity is way too much #################


#   PAGERANK

G = nx.barabasi_albert_graph(len(def_urls),76)
pr = nx.pagerank(G,0.4)
pr_values = list(pr.values())
dic = {}
for i in range(len(def_urls)):
    dic[def_urls[i]]=pr_values[i]

dic = dict(sorted(dic.items(), key=lambda item: item[1]))
# print(dic)

sorted_scores = []

for link,pr_score in dic.items():
    t = []
    t.append(pr_score)
    t.append(link)
    sorted_scores.append(t)

sorted_scores.sort()
sorted_scores.reverse()
# for score in sorted_scores:
#     print(score)

count = len(sorted_scores)//20


test_links=[]
for i in range(count):
    test_links.append(sorted_scores[i])

# print(test_links)

# for u in test_links:
#     print(u)

test_def = {}

for i in range(count):
    req_test = requests.get(test_links[i][1], headers)
    soup_test = BeautifulSoup(req_test.content, 'html.parser')
    test_def[test_links[i][1]] = soup_test.find("div",{"id":"mw-content-text"})
    
for link,definition in test_def.items():
    temp = []
    temp.append(dic[link])
    temp.append(definition.find('p').text)
    test_def[link] = temp

print(test_def)