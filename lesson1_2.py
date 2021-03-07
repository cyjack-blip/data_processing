# Урок 1, Задание 2
# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
#

import requests
import json
from pprint import pprint

# Yahoo-finance. Auto-complete запрос: получение новостей по ключевому слову и список найденых компаний с этим словом

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

headers = {
    'x-rapidapi-key': "0b7bd705e9msh3823599c8ccff3cp12ce04jsnd51379a63e1c",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open('market_news.json', 'w') as f:
    json.dump(response.json(), f)

pprint(response.json())
