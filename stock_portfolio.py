import json
import os

class StockPortfolio:
    def __init__(self, portfolio_file):
        self.portfolio_file = portfolio_file
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        if os.path.exists(self.portfolio_file):
            with open(self.portfolio_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_portfolio(self):
        with open(self.portfolio_file, 'w') as f:
            json.dump(self.portfolio, f)

    def add_stock(self, symbol, quantity, price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'price': price}

        self.save_portfolio()

    def view_portfolio(self):
        print("Stock Portfolio:")
        for symbol, stock in self.portfolio.items():
            print(f"{symbol}: {stock['quantity']} shares @ ${stock['price']}")

    def generate_report(self):
        print("Stock Portfolio Report:")
        total_value = 0
        for symbol, stock in self.portfolio.items():
            value = stock['quantity'] * stock['price']
            total_value += value
            print(f"{symbol}: {stock['quantity']} shares @ ${stock['price']} = ${value:.2f}")

        print(f"Total value: ${total_value:.2f}")