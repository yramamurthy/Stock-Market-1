from core.exception.InstrumentError import InstrumentError
from core.kite.Instrument import Instrument


class Instruments:

    def __init__(self, db, kite, positions):
        self.db = db
        self.kite = kite
        self.positions = positions
        self.instrument_list = []

    def get_instrument(self, instrument_token=None, instrument_symbol=None):
        if instrument_token is None and instrument_symbol is None:
            raise InstrumentError()

        instrument_dict = self.db.get_instrument(instrument_token=instrument_token, instrument_symbol=instrument_symbol)
        instrument_token = instrument_dict['instrument_token']

        for instrument in self.instrument_list:
            if instrument_token == instrument.instrument_token:
                return instrument

        instrument_symbol = instrument_dict['tradingsymbol']
        name = instrument_dict['name']
        instrument = Instrument(instrument_token, instrument_symbol, name, self.kite, self.positions)
        self.instrument_list.append(instrument)
        return instrument

    def refresh_instruments(self):
        instruments = self.kite.data_api.instruments()
        self.db.refresh_instruments(instruments)
