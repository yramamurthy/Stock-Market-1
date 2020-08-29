import pymongo

from core.exception.DBError import DBInstrumentError
from core.util.Time import Time


class DB:

    def __init__(self):
        mongo = pymongo.MongoClient()
        self.db = mongo["StockMarket"]

    def get_application_config(self):
        self.db["config"].find_one()

    def update_token(self, user_id, access_token):
        self.db["config"].update_one({'user_id': user_id},
                                     {'$set': {'access_token': access_token,
                                               'last_updated': str(Time.today())}})

    def get_instrument(self, instrument_token=None, instrument_symbol=None):
        if instrument_token is not None:
            return self.db["stocks"].find_one({'instrument_token': instrument_token, 'exchange': 'NSE'})
        elif instrument_symbol is not None:
            return self.db["stocks"].find_one({'tradingsymbol': instrument_symbol, 'exchange': 'NSE'})
        else:
            raise DBInstrumentError()

    def refresh_instruments(self, instrument_list):
        instruments = self.db["stocks"]
        instruments.drop()
        for x in instrument_list:
            try:
                x["expiry"] = str(x["expiry"])
                instruments.insert_one(x)
            finally:
                pass
