import os
# small cleanup

class Config:
    def __init__(self):
        self.alpha_vantage_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
        self.portfolio_file = os.environ.get('PORTFOLIO_FILE')

# leaving a note for later
    def get_alpha_vantage_api_key(self):
        return self.alpha_vantage_api_key

# was easier to read this way
    def get_portfolio_file(self):
        return self.portfolio_file