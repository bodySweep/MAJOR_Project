import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time

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
for para in paras:
    print(para)
    print()


# replace_text = " this is the definition"
# text = para.get_text()

# print(len(text))
# print(text)


# for link in links:
#     text = text.replace(link.string, link.string+replace_text, 1)
# print(text)
# engine.say(text)
# engine.runAndWait()

