import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

url = 'https://us.econoday.com/byweek.asp?cust=us'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

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