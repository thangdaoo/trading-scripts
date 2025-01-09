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

for garbage in soup.findAll(['div', 'span'], {'class': ['econoitems', 'banknotefont']}):
    garbage.decompose()

unformatted_data = []
for event in soup.find_all('td', class_='events'):
    eventName = event.text.replace('»', '').replace('Market Focus', '').replace('Market Reflections', '').replace('Global Economics', '').lstrip()
    eventName = re.split('(\d+\:\d+\s\w+\s\w\w)', eventName)
    unformatted_data.append(eventName)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for idx, day in enumerate(unformatted_data):
    for i in range(0, len(day), 2):
        if i+1 < len(day):
            formatted_data.append([days[idx], day[i], day[i+1]])

df = pd.DataFrame(formatted_data, columns=['Day', 'Event', 'Time'])

while True:
    selection = input("Enter '1' to view this week's events or '2' to view only today's events: ")
    if selection == '1':
        print(df.to_string(index=False))
        break
    elif selection == '2':
        today = datetime.datetime.today()
        day_of_week = today.strftime("%A")
        todays_events = df.loc[df['Day'] == day_of_week]
        todays_events = todays_events.drop(columns=['Day'])
        print(todays_events.to_string(index=False))
        break
    else:
        print("Invalid input. Please enter '1' or '2'.")