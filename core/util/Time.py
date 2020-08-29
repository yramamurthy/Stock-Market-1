from datetime import datetime, timedelta
import time


class Time:

    @staticmethod
    def today():
        today = datetime.today()
        return today

    @staticmethod
    def day_before_today(no_of_days):
        day = datetime.today() - timedelta(days=no_of_days)
        return day

    @staticmethod
    def day_after_today(no_of_days):
        day = datetime.today() + timedelta(days=no_of_days)
        return day

    @staticmethod
    def format(date_time):
        date_time = date_time.strftime("%Y-%m-%d")
        return date_time

    @staticmethod
    def format_with_time(date_time):
        date_time = date_time.strftime("%Y-%m-%d 00:00:00")
        return date_time

    @staticmethod
    def convert_to_time(str_time):
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')

    @staticmethod
    def calculate_time_consumed(func):
        def inner1(*args, **kwargs):
            begin = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("Total time consumed in : ", func.__name__, end - begin)

        return inner1
