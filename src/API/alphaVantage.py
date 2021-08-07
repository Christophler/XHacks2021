
import requests

def timeSeriesDailyAdjusted():
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=U4FVM2VFYLRW4T31'
  r = requests.get(url)
  data = r.json()

  print(data)


def exchangeRates():
  url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CAD&apikey=U4FVM2VFYLRW4T31'
  r = requests.get(url)
  data = r.json()

  print(data)

def quotePrice(sym):
  url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+sym+'&apikey=U4FVM2VFYLRW4T31'
  r = requests.get(url)
  data = r.json()

  print(data)