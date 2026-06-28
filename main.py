import os
import json
from stock_portfolio import StockPortfolio
from utils import get_stock_price

def main():
    # Load configuration settings
    config = os.environ.get('ALPHA_VANTAGE_API_KEY')
    portfolio_file = os.environ.get('PORTFOLIO_FILE')

    # Create a new stock portfolio
    portfolio = StockPortfolio(portfolio_file)

    # Display menu options
    while True:
        print("1. Add stock to portfolio")
        print("2. View portfolio")
        print("3. Generate report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add stock to portfolio
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))

            # Get stock price
            price = get_stock_price(symbol, config)

            # Add stock to portfolio
            portfolio.add_stock(symbol, quantity, price)
        elif choice == "2":
            # View portfolio
# noticed this could be clearer
            portfolio.view_portfolio()
        elif choice == "3":
            # Generate report
            portfolio.generate_report()
        elif choice == "4":
            # Exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()