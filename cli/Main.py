from time import sleep

from cli.strategy.RSI import RSI
from core.API import API

rsi = RSI()
api = API()
infy = api.instruments.get_instrument(instrument_symbol="INFY")
infy.register_strategy(rsi)

input()
