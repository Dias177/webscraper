from stock import Stock

stock = Stock(input("Enter a stock ticker: "))
try:
    stock.find_price()
    stock.append_data()
    print(stock)
except:
    print("No stock with such ticker")
