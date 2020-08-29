from core.util.Time import Time


def update_instruments_value(data, instruments):
    for tick in data:
        instrument_token = tick["instrument_token"]
        instrument = instruments.get_instrument(instrument_token=instrument_token)
        data = {'price': tick["last_price"], 'volume': tick["last_quantity"], 'time': Time.today()}
        instrument.update_quotes(data)
