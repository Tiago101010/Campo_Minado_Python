import requests

resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()
print(resposta)

compra = resposta["USDBRL"]["bid"]
venda = resposta["USDBRL"]["ask"]

print(compra," ",venda)