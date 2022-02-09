  
 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import tweepy
import time


def getPrices():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
   'symbol' : 'btc,eth,doge,xno,ada,matic'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b59bbd74-057c-4b56-853a-4d5490330487',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    jsdata = json.loads(response.text)
    global BTC, ETH, DOGE, ADA, XNO
    BTC  = round(jsdata["data"]["BTC"]["quote"]["USD"]["price"],2)
    ETH = round(jsdata["data"]["ETH"]["quote"]["USD"]["price"],2)
    DOGE = round(jsdata["data"]["DOGE"]["quote"]["USD"]["price"],5)
    ADA = round(jsdata["data"]["ADA"]["quote"]["USD"]["price"],2)
    XNO = round(jsdata["data"]["XNO"]["quote"]["USD"]["price"],2)


  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
    print ("ran out of credits")

def currentTime():
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  return current_time




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)
myTime = currentTime()
#getPrices(BTC, ETH, DOGE, ADA, NANO)
getPrices()
twitter_API.update_status('Current prices as of ' + myTime + "PST\n BTC: $" + str(BTC) + "\n ETH: $" + str(ETH) +  "\n DOGE: $" + str(DOGE) + "\n ADA: $" + str(ADA) + "\n NANO: $" + str(XNO))

#twitter_API.update_status('Hi im EddieBot')



