import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'v2=1495343816.182.19.234.142',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': "https://finviz.com/"
}

def getNews():
    while True:
        ticker = input("Enter the stock ticker: ")
        if ticker.isalpha():
            break

    url = 'https://finviz.com/quote.ashx?t=' + ticker
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    news = []

    for articles in soup.findAll('table', id="news-table"):
        news.append(articles.text)

    # reverse prints array so news is in descending order
    for i in range(len(news)-1,-1,-1):
        print(news[i])

while True:
    try:
        getNews()
        response = input("Press any key to continue or press 'q' to exit: ")
        if response == 'q':
            break
    except Exception:
        getNews()
