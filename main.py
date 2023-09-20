import requests, json, locale

valorConvertido = valorConverter = 0
moeda = simbolo = ''
url = requests.get(f'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL').json()

cotacaoDolar = float(url['USDBRL']['bid'])
cotacaoEuro = float(url['EURBRL']['bid'])
cotacaoBitcoin = float(url['BTCBRL']['bid'])

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(f'US$ Dólar Hoje: {locale.currency(cotacaoDolar)}')
print(f'€ Euro Hoje: {locale.currency(cotacaoEuro)}')
print(f'₿ Bitcoin Hoje: {locale.currency(cotacaoBitcoin)}')
print('-' * 60)

valorConverter = float(input('Informe um valor em reais para converter: R$  '))

def converter_dinheiro(cotacaoMoeda):
    valorConvertido = valorConverter / cotacaoMoeda
    return float(valorConvertido)
    
def resultado():
    print(f'{"RESULTADO":-^70}')
    if moeda == 'bitcoin(s)':
        print(f'R$ {locale.currency(valorConverter)} real(is), equivale a {simbolo} {valorConvertido:.4f} {moeda}')
    else:
        print(f'R$ {locale.currency(valorConverter)} real(is), equivale a {simbolo} {locale.currency(valorConvertido)} {moeda}')

while True:
    print(f'\n{"CONVERSOR DE MOEDAS":-^70}')
    opcao = int(input(
        """
        [1] - Converter Real R$ para Dólar(es) US$
        [2] - Converter Real R$ para Euro(s) €
        [3] - Converter Real R$ para Botcoin(s) ₿
        [0] - Sair
        Opção: """))
    if opcao == 0:
        break
    elif opcao == 1:        
        moeda = 'dólar(es)'
        simbolo = 'US$'
        valorConvertido = converter_dinheiro(cotacaoDolar)
        resultado()
    elif opcao == 2:        
        moeda = 'euro(s)'
        simbolo = '€'
        valorConvertido = converter_dinheiro(cotacaoEuro)
        resultado()
    elif opcao == 3:        
        moeda = 'bitcoin(s)'
        simbolo = '₿'
        valorConvertido = converter_dinheiro(cotacaoBitcoin)
        resultado()
    else:
        print('Opção inválida, informe uma opção válida!')
print(f'{"FIM":-^70}')