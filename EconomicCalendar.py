import requests
import re
from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://us.econoday.com/byweek.asp?cust=us'

curDate = date.today()
curDate = curDate.strftime('%A %b %d')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekdayCounter = 0

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

# for event in soup.find_all('td', class_='events'):
#     eventName = event.text
#     eventName.split('')
#     print(days[weekdayCounter])
#     print(eventName)
#     print('-------------')
#     weekdayCounter += 1

event = soup.find('td', class_='events')
eventName = event.text
eventName.type
print(eventName)

