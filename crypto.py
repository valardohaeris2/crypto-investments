import requests
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query/"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = "" 
TWILIO_AUTH_TOKEN = ""

crypto_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "ETH",
    "market": "USD",
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=crypto_params)
data = response.json()

print(data)
