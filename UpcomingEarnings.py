import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Upgrade-Insecure-Requests': '1', 'Cookie': 'v2=1495343816.182.19.234.142', 'Accept-Encoding': 'gzip, deflate, sdch',
        'Referer': "https://seekingalpha.com/earnings/earnings-calendar"}

symbols = []
names = []
release_dates = []
release_times = []
        
def getEarnings():
    while True:
        page_num = input("Select a page: ")
        if page_num.isdigit():
            break

    url = 'https://seekingalpha.com/earnings/earnings-calendar/' + page_num
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    for symbol in soup.findAll('td', class_='pad-left symbol'):
        symbols.append(symbol.text)

    for name in soup.findAll('td', class_='name'):
        names.append(name.text)

    for rlsdte in soup.findAll('span', class_='release-date'):
        release_dates.append(rlsdte.text)

    for rlstme in soup.findAll('span', class_='release-time'):
        release_times.append(rlstme.text)

    d = {'Symbol': symbols, 'Name': names, 'Release Date': release_dates, 'Release Time': release_times}
    df = pd.DataFrame(d)
    pd.set_option("max_colwidth", 39)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
        

while True:
    try:
        getEarnings()
        response = input("Press any key to continue or press 'q' to quit: ")
        if response == 'q':
            break
    except Exception:
        getEarnings()
