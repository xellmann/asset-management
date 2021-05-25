import requests

headers = {
    'X-CMC_PRO_API_KEY': '438fa224-2803-47df-8395-a25215a729f4',
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

#print(json)

coins = json['data']

for x in coins:
    if x['symbol'] == 'BTC':
        print(x['symbol'], x['quote']['USD']['price'])
        btc_price = x['symbol'], x['quote']['USD']['price']
    print(x['symbol'], x['quote']['USD']['price'])

