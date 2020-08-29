import os
import tempfile
from datetime import datetime
import pandas as pd

from core.util.Time import Time


class Instrument:

    def __init__(self, instrument_token, instrument_symbol, name, kite, positions):
        self.instrument_token = instrument_token
        self.instrument_symbol = instrument_symbol
        self.kite = kite
        self.name = name
        self.positions = positions
        self.strategy_list = []
        self.quotes = []

    def update_quotes(self, data):
        self.quotes.append(data)
        self.positions.notify_update(self)
        for strategy in self.strategy_list:
            strategy.notify_update(self)

    def register_strategy(self, strategy):
        self.strategy_list.append(strategy)

    def get_historical_data(self, instrument_token, interval="day", lmt=0, force_download=False):
        from_date = Time.format(Time.day_before_today(lmt))
        to_date = Time.format(Time.day_after_today(1))
        name = str(instrument_token) + "_" + str(from_date) + "_" + str(to_date) + interval + str(lmt)
        name = os.path.join(tempfile.gettempdir(), name + ".csv")
        if os.path.isfile(name) and datetime.fromtimestamp(
                os.path.getmtime(name)).date() == datetime.today().date() and not force_download:
            df = pd.read_csv(name)
        else:
            df = pd.DataFrame(self.kite.data_api.historical_data(instrument_token, from_date, to_date, interval))
            df.to_csv(name, index=False)
        df["date"] = pd.to_datetime(df["date"])
        return df
