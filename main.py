import os
from pathlib import Path
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from cryptorank import api
from html import create_html

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

API_KEY_CRYPTORANK = os.getenv('API_KEY_CRYPTORANK')


def save_file(name, data):
    f = open(BASE_DIR / name, 'w')
    f.write(data)
    f.close()


response = api.get_currencies(API_KEY_CRYPTORANK, 3)
if response.status_code == 200:
    columns = ['Наименование', 'Тег', 'Timestamp']
    data = []
    for currency in response.json().get('data'):
        data.append({'Наименование': currency.get("name"), 'Тег': currency.get("symbol"),
                     'Timestamp': currency.get("lastUpdated")})
    data_html = create_html.create(columns, data)
    save_file('cryptorank.html', data_html)
    print('Создан файл cryptorank.html')

else:
    print(f' Error:{response.status_code} {response.content}')

cg = CoinGeckoAPI()
columns = ['Наименование', 'Цена', 'Timestamp']
data = []
for currency in cg.get_coins()[:65]:
    data.append(
        {'Наименование': currency.get("name"), 'Цена': currency.get("market_data").get("current_price").get("usd"),
         'Timestamp': currency.get("last_updated")})

data_html = create_html.create(columns, data)
save_file('CoinGecko.html', data_html)
print('Создан файл CoinGecko.html')
