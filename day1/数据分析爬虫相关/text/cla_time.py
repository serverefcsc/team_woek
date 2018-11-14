import time


def cal_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return

    return inner
