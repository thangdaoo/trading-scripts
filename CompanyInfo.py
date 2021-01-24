import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup as bs
import requests
from bs4 import BeautifulSoup

def switch():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Upgrade-Insecure-Requests': '1', 'Cookie': 'v2=1495343816.182.19.234.142', 'Accept-Encoding': 'gzip, deflate, sdch',
                'Referer': "http://finviz.com/quote.ashx?t="}
        while True:
            stock = input("Enter the stock ticker: ")
            if stock.isalpha():
                break

        url = 'https://finviz.com/quote.ashx?t=' + stock
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        print("1 - Company Bio\n2 - Financials")
        option = int(input('Select an option: '))

        def getBio():
            bio = soup.find('td', class_='fullview-profile')
            print(bio.text)

        def getFinancials():
            datas = []
            headers = []

            for header in soup.findAll('td', class_='snapshot-td2-cp'):
                headers.append(header.text)
            for data in soup.findAll('td', class_='snapshot-td2'):
                datas.append(data.text)

            d = {'Header':headers,'Data':datas}
            df = pd.DataFrame(d)

            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df)

        def error():
            print("Invalid option, please try again")

        dict = {
            1 : getBio,
            2 : getFinancials
        }
        dict.get(option,error)()

    except Exception as error:
        print("Invalid entry. Please try again.")

switch()
