from threading import Thread
from queue import Queue


class TaskManager:

    def __init__(self, no_of_workers=10):
        self.no_of_workers = no_of_workers
        self.queue = Queue()

    def worker(self):
        while True:
            fun, *pram = self.queue.get()
            fun(*pram)

    def start(self):
        for i in range(self.no_of_workers):
            worker = Thread(target=self.worker)
            worker.setDaemon(True)
            worker.start()
