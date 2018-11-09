import urllib
import csv
from datetime import datetime
from bs4 import BeautifulSoup


stock_ticker = input("Enter a stock ticker: ")

url = 'http://kase.kz/ru/shares/show/' + stock_ticker + '/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

ticker = soup.find("h1", attrs={"style": "text-transform: none;"})
ticker = ticker.text.strip()
print(ticker)

price = soup.find("div", attrs={"class": "h1-block__indicator"})
price = price.text.strip()
print(price)

with open('stock.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([ticker, price, datetime.now()])
