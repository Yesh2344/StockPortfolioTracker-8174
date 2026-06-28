import requests

def get_stock_price(symbol, api_key):
# cleaner this way
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return float(data['Global Quote']['05. price'])
    else:
        return None