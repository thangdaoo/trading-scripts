import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Upgrade-Insecure-Requests': '1', 'Cookie': 'v2=1495343816.182.19.234.142', 'Accept-Encoding': 'gzip, deflate, sdch',
           'Referer': "https://us.econoday.com/byweek.asp?cust=us"}
url = 'https://us.econoday.com/byweek.asp?cust=us'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.content, "html.parser")

week = []

for garbage in soup.findAll('div', class_='econoitems'):
    garbage.decompose()

for garbage in soup.findAll('span', class_='banknotefont'):
    garbage.decompose()

for event in soup.find_all('td', class_='events'):
    eventName = event.text
    eventName = eventName.replace('»', '')
    eventName = eventName.replace('Market Focus', '')
    eventName = eventName.replace('Market Reflections', '')
    eventName = eventName.replace('Global Economics', '')
    eventName = eventName.lstrip()
    eventName = re.split('(\d+\:\d+\s\w+\s\w\w)', eventName)
    week.append(eventName)

mon = {'Monday': week[0]}
tues = {'Tuesday': week[1]}
wed = {'Wednesday': week[2]}
thurs = {'Thursday': week[3]}
fri = {'Friday': week[4]}

monday = pd.DataFrame(mon)
tuesday = pd.DataFrame(tues)
wednesday = pd.DataFrame(wed)
thursday = pd.DataFrame(thurs)
friday = pd.DataFrame(fri)

weekday_events = [monday,tuesday,wednesday,thursday,friday]

for x in weekday_events:
    print(x.to_string(index=False))