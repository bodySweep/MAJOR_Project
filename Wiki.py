import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time
from prototype_link_extracter import link_extractor
import networkx as nx
import wikipediaapi
from nltk.tokenize import sent_tokenize

wiki = wikipediaapi.Wikipedia('en')
# page_wiki = wiki.page("Udaipur")
# res = sent_tokenize(page_wiki.summary);
# print(res)

url = "https://en.wikipedia.org/wiki/Delhi"
html_content = requests.get(url).text
soup = bs(html_content, 'html.parser')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 150)

# s = "This is a string."
# result = s.split(" ")
# print(result)

paras = soup.find_all("p")
main_para = []
for para in paras:
    if len(para.get_text()) > 50:
        # engine.say(para.get_text())
        main_para.append(para)
# print(main_para[1])
# print(main_para[0])



para = main_para[1]
links = main_para[1].find_all("a", href=True)

list_dict = {}
list_of_links = []
for item in links:
    print(item['href'])
    if item['href'].startswith("#"):
        continue
    else:
        list_of_links.append(item.string)

for item in list_of_links:
    print(item)
    page_wiki = wiki.page(item)
    list_dict[item] = page_wiki.summary;

print(list_dict['Purana Qila'])


# replace_text = " this is the definition"
text = para.get_text()
text = sent_tokenize(text);

print(text)

final_string = ""

for line in text:
    final_string += line + " "
    for i in range(len(list_of_links)):
        if list_of_links[i] in line:
            final_string += list_dict[list_of_links[i]] + " "

print(final_string)


engine.say(final_string)
engine.runAndWait()
