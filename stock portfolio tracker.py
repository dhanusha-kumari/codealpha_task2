

class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

    def __str__(self):
        return f"{self.symbol}: {self.shares} shares"

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol].shares += shares
        else:
            self.stocks[symbol] = Stock(symbol, shares)

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            if self.stocks[symbol].shares >= shares:
                self.stocks[symbol].shares -= shares
                if self.stocks[symbol].shares == 0:
                    del self.stocks[symbol]
            else:
                print(f"Not enough shares to remove. You have {self.stocks[symbol].shares} shares of {symbol}.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def view_portfolio(self):
        if not self.stocks:
            print("Your portfolio is empty.")
            return
        print("Your Portfolio:")
        for stock in self.stocks.values():
            print(stock)

    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        return stock.history(period="1d")['Close'].iloc[-1]

    def view_portfolio_value(self):
        total_value = 0
        for stock in self.stocks.values():
            price = self.get_stock_price(stock.symbol)
            total_value += price * stock.shares
            print(f"{stock.symbol}: {stock.shares} shares @ ${price:.2f} = ${price * stock.shares:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = Portfolio()
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. View Portfolio Value")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.view_portfolio()
        elif choice == '4':
            portfolio.view_portfolio_value()
        elif choice == '5':
            print("Exiting the portfolio tracker.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
