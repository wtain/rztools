import configparser
import threading
from time import sleep

config = configparser.RawConfigParser()
config.read('app.properties')

pool_time = int(config.get('Scheduler', 'scheduler.pool_time_seconds'))

def worker():
    print("Worker thread started")
    while True:
        print(f"Sleeping {pool_time} seconds")
        sleep(pool_time)


worker_thread = threading.Thread(target=worker)
worker_thread.start()
