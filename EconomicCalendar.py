import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Upgrade-Insecure-Requests': '1', 
    'Cookie': 'v2=1495343816.182.19.234.142', 
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': "https://us.econoday.com/byweek.asp?cust=us"
    }

url = 'https://us.econoday.com/byweek.asp?cust=us'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.content, "html.parser")

unformatted_data = []
formatted_data = []

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
    unformatted_data.append(eventName)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for idx, day in enumerate(unformatted_data):
    for i in range(0, len(day), 2):
        if i+1 < len(day):
            formatted_data.append([days[idx], day[i], day[i+1]])

df = pd.DataFrame(formatted_data, columns=['Day', 'Event', 'Time'])

selection = input("Enter '1' to view this weeks events or '2' to view only today's events: ")
if selection == '1':
    print(df.to_string(index=False))
elif selection == '2':
    today = datetime.datetime.today()
    day_of_week = today.strftime("%A")
    todays_events = df.loc[df['Day'] == day_of_week]
    todays_events = todays_events.drop(columns=['Day'])
    print(todays_events.to_string(index=False))