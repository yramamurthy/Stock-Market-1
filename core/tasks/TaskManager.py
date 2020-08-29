from threading import Thread
from queue import Queue

from core.tasks.Tasks import update_instruments_value


class TaskManager:
    TASK1 = 1

    def __init__(self, instruments, no_of_workers=10):
        self.no_of_workers = no_of_workers
        self.queue = Queue()
        self.instruments = instruments

    def worker(self):
        while True:
            data, task_type = self.queue.get()

            if task_type == self.TASK1:
                update_instruments_value(data, self.instruments)

    def start(self):
        for i in range(self.no_of_workers):
            worker = Thread(target=self.worker)
            worker.setDaemon(True)
            worker.start()
