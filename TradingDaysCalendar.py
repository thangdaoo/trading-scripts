import requests
import re
from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.swingtradesystems.com/trading-days-calendars.html'

curDate = date.today()
curDate = curDate.strftime('%A, %B %d')

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

print('----------------------------------------------------')
print('TODAY\'S DATE: ' + curDate)
print('----------------------------------------------------')

remainingTradeDays = soup.find('p', class_="center fontsize3").text
remainingTradeDays = remainingTradeDays.replace('***', '')
print(remainingTradeDays)

info = soup.find('div', class_="calbox blockcenter1 center")
print(info.text)

print('NOTE: Regular market hours are 9:30am–4:00pm EST. Short sessions end at 1:00pm EST.')
