import logging


# from core.util.Time import Time


class Logger:
    INFO = 1
    WARNING = 2
    ERROR = 3

    def __init__(self):
        pass

    def log(self, message, level=INFO):
        self.db["log"].insert_one({'message': message, 'level': level, 'time': str(Time.today())})

    def get_logs(self):
        return self.db["log"].find()
