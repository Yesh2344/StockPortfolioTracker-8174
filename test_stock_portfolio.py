import unittest
from stock_portfolio import StockPortfolio

class TestStockPortfolio(unittest.TestCase):
    def test_add_stock(self):
        portfolio = StockPortfolio('test_portfolio.json')
        portfolio.add_stock('AAPL', 10, 100.0)
        self.assertEqual(portfolio.portfolio['AAPL']['quantity'], 10)
        self.assertEqual(portfolio.portfolio['AAPL']['price'], 100.0)

    def test_view_portfolio(self):
        portfolio = StockPortfolio('test_portfolio.json')
        portfolio.add_stock('AAPL', 10, 100.0)
        portfolio.add_stock('GOOG', 5, 2000.0)
        portfolio.view_portfolio()

    def test_generate_report(self):
        portfolio = StockPortfolio('test_portfolio.json')
        portfolio.add_stock('AAPL', 10, 100.0)
        portfolio.add_stock('GOOG', 5, 2000.0)
        portfolio.generate_report()

if __name__ == '__main__':
    unittest.main()