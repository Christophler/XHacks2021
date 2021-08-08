
import requests

def timeSeriesDailyAdjusted(sym):
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+sym+'&apikey=U4FVM2VFYLRW4T31'
  r = requests.get(url)
  data = r.json()

  # print(data)
  return data

def getPoints(numPoints, stockName):
  json = timeSeriesDailyAdjusted(stockName)
  dayData = json['Time Series (Daily)']
  points = []
  c = 0
  for date in dayData:
    if c < numPoints:
      point = dayData[date]['2. high']
      points.append(point)
      c += 1
    else:
      break
  return points