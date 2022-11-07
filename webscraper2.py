from bs4 import BeautifulSoup
import requests
import validators
import re
import random


def scrapetillrick(link, count):
    print(count)
    webpage = requests.get(link)
    scraper = BeautifulSoup(webpage.content, 'html.parser')
    allLinks = scraper.find('div', id = "mw-content-text").find_all(href = re.compile("/wiki/"))
    random.shuffle(allLinks)
    firstlink = allLinks[0]
    while(':' in firstlink['href']):
       random.shuffle(allLinks)
       firstlink = allLinks[0] 

    if(count == 10):
        print(scraper.find(href = re.compile("/wiki/"))['href'])
        return "you failed"
    if(scraper.find(href = re.compile("/wiki/"))['href'] != "//en.m.wikipedia.org/wiki/Never_Gonna_Give_You_Up"):
        count += 1
        print("https://en.m.wikipedia.org" + firstlink['href'])
        return scrapetillrick("https://en.m.wikipedia.org" + firstlink['href'], count)
    else:
        print(scraper.find(href = re.compile("/wiki/"))['href'])
        return "Yay! I knew you would never give up"

print("please enter a url")
link = input()
while((validators.url(link)) != True):
    print("Sorry, invalid url. Please try again")
    link = input()
print(scrapetillrick(link, 0))

