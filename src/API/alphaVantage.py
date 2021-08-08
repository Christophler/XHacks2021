
import requests

def timeSeriesDailyAdjusted(sym):
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+sym+'&apikey=U4FVM2VFYLRW4T31'
  r = requests.get(url)
  data = r.json()

  # print(data)
  return data