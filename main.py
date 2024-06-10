from forex_python.converter import CurrencyRates
valor = str(input('informe o valor de moeda a ser convertido: '))
valor = float(valor.replace(',','.')).upper()
moeda_origem = input('informe a moeda de destino: ').upper()
moeda_destino = input('informe a moeda de destino: ').upper()

#faz a conversão
result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

#exibe o resultado
print(f'$ {valor:,.2f} {moeda_origem} = $ {result:,.2f} {moeda_destino}.')