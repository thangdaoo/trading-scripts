import requests
import re
from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://us.econoday.com/byweek.asp?cust=us'

curDate = date.today()
curDate = curDate.strftime('%A %b %d')

days = ['-----MONDAY-----', '-----TUESDAY-----', '-----WEDNESDAY-----', '-----THURSDAY-----', '-----FRIDAY-----']
weekdayCounter = 0

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

print('-----------')
print('Today\'s Date: ' + curDate)
print('-----------')

for event in soup.find_all('td', class_='events'):
    eventName = event.text
    eventName = eventName.replace('»', '')
    eventName = eventName.replace('Market Focus', '')
    eventName = eventName.replace('Market Reflections', '')
    eventName = eventName.replace('Global Economics', '')
    eventName = eventName.lstrip()
    eventName = re.split('(\d+\:\d+\s\w+\s\w\w)', eventName)
    print(days[weekdayCounter]+'\n')
    for index, piece in enumerate(eventName):
        print(piece)
        if index % 2 != 0:
            print('-----')
    weekdayCounter += 1


# Tried to remove unnecessary tags

# for event in soup.find_all('td', class_='events'):
#     # print(soup.find('span', class_ = 'banknotefont'))
#     event = event.prettify()
#     print(event)
#     print('----------')

# for garbage in soup.find_all('span', class_='banknotefont'):
#     print(garbage)
#     print('---------')