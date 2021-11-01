import logging
import threading
import time

class ThreadTests:
    def __init__(self):
        self.lock = threading.Lock()

    def thread_function(self, name):
        self.lock.acquire()
        logging.info("Function %s: starting", name)
        time.sleep(2)
        logging.info("Function %s: finishing", name)
        self.lock.release()


    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
    logging.info("Main    : create and start thread %s.", "szukanie celu")
    x = threading.Thread(target=thread_function, args=("szukanie celu",))
    y = threading.Thread(target=thread_function, args=("centrowanie kamery",))
    x.start()
    y.start()
    x.join()
    y.join()
