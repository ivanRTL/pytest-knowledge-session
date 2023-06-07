import time

class Database:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        time.sleep(2000)
        return ["data"]
        