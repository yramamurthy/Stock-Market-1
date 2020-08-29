"""
 subscribe to 200 instruments
 3 connections.
 200 order placement per minute
 2000 MIS orders per day and 2000 BO/CO per day limit.
"""


# TODO :: kws.on_order_update = on_order_update
class Socket:

    def __init__(self, socket_api, task_manager):
        self.socket_api = socket_api
        self.task_manager = task_manager
        self.subscribe_stocks_list = []
        self.log = None

    def on_ticks(self, ws, ticks):
        self.task_manager.queue.put_nowait((ticks, self.task_manager.TASK1))

    def on_connect(self, ws, response):
        self.log.print("Connected to the Socket", self.log.INFO)

    def on_close(self, ws, code, reason):
        self.log.print("Disconnected from the Socket. Reason :: " + str(reason), self.log.ERROR)
        ws.stop()

    def subscribe_stock(self, instrument_token):
        self.subscribe_stocks_list.append(int(instrument_token))
        self.socket_api.subscribe([int(instrument_token)])
        # self.socket_api.set_mode(self.socket_api.MODE_FULL, [int(instrument_token)])

    def unsubscribe_stock(self, instrument_token):
        self.socket_api.unsubscribe([int(instrument_token)])

    def start(self):
        self.socket_api.on_ticks = self.on_ticks
        self.socket_api.on_connect = self.on_connect
        self.socket_api.on_close = self.on_close
        self.socket_api.connect(threaded=True)
