import os
from dotenv import load_dotenv
from binance.spot import Spot

load_dotenv()

API = os.getenv('API_TOKEN')
API_NAME = os.getenv('TOKEN_NAME')


client = Spot()

# Get server timestamp
# print(client.time())
# Get klines of BTCUSDT at 1m interval
# print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# API key/secret are required for user data endpoints
client = Spot(api_key=API_NAME, api_secret=API)

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}
