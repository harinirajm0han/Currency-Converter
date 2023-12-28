import requests
API_KEY='fca_live_UAoknfnZZwflFXNvaZWhQ5ji0lFKiJ1JIgq6u71D'
BASE_URL=f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
#CURRENCIES=["USD","CAD","EUR","AUD","CNY","INR","THB","TRY","GBP","BGN","HRK","CYP","CZK","DKK","EEK","HUF","ISK","IDR","JPY","KRW","LVL","LTL","MYR","MTL","NZD","NOK","PHP","PLN","RON","RUB","SGD","SKK","SIT","ZAR","SEK","CHF","THB","TRY","GBP"]
CURRENCIES=["USD","CAD","EUR","AUD","CNY"]
def convert_currency(base):
    currencies=",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response=requests.get(url)
        data=response.json()
       # print(data)
        return data["data"]
    except Exception as e:
        print(e)
        print("Invalid currency")
        return None

#data=convert_currency("CAD")
#print(data)
while True:
    base=input("Enter the base currency (q for quit):").upper()
    if base=="Q":
        break
    data=convert_currency(base)
    for ticker,value in data.items():
        print(f"{ticker}:{value}")