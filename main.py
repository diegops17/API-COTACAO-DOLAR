import requests
import json
import locale

url = requests.get(f'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL').json()
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(f"Cotação do Dólar US$ {locale.currency(float(url['USDBRL']['bid']))}")
print(f"Cotação do Euro € {locale.currency(float(url['EURBRL']['bid']))}")
print(f"Cotação do Bitcoin ₿ {locale.currency(float(url['BTCBRL']['bid']))}")
