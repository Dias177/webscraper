from stock import Stock
import lst

print("Most liquid stocks: ")
print(lst.most_liquid())
stock = Stock(input("Enter a stock ticker from the list above: "))
try:
    stock.find_price()
    stock.append_data()
    print(stock)
except:
    print("No stock with such ticker")
