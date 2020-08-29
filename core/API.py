from core.db.DB import DB
from core.kite.Instruments import Instruments
from core.kite.Kite import Kite
from core.kite.Socket import Socket
from core.positions.Positions import Positions
from core.tasks.TaskManager import TaskManager
from core.util.Logger import Logger


class API:

    def __init__(self):
        self.db = DB()
        self.kite = Kite(self.db)
        self.positions = Positions()
        self.logger = Logger()
        self.instruments = Instruments(self.db, self.kite, self.positions)
        self.task_manager = TaskManager(self.instruments)

        self.socket = Socket(self.kite.socket_api, self.task_manager)
        self.socket.start()
