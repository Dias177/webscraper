import urllib
import csv
from datetime import datetime
from bs4 import BeautifulSoup

def find_price(stock_ticker):

    url = "http://kase.kz/ru/shares/show/" + stock_ticker + "/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    ticker = soup.find("h1", attrs={"style": "text-transform: none;"})
    ticker = ticker.text.strip()


    price = soup.find("div", attrs={"class": "h1-block__indicator"})
    price = price.text.strip()

    return price

def append_data(stock_ticker, price):
    with open("stock.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([ticker, price, datetime.now()])


ticker = input("Enter a stock ticker: ")
try:
    price = find_price(ticker)
    print("Price of " + ticker + ": " + price)
    append_data(ticker, price)
except:
    print("No stock with such ticker")
