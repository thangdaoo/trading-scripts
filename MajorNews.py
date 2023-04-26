import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'v2=1495343816.182.19.234.142',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': "https://finviz.com/"
}

def getMajorNews():
    url = 'https://finviz.com/'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    major_news = []

    for tickers in soup.find_all('tr', class_="table-light-row-cp"):
        print(tickers)

getMajorNews()