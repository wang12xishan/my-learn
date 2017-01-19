import multiprocessing
import time


class MyProcessing(multiprocessing.Process):
    def __init__(self):
        super().__init__(self)

    def run(self):
        pass




if __name__ == '__main__':
    p = MyProcessing()
    q = multiprocessing.Queue