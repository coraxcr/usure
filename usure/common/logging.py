import logging
import time
import warnings
from os import path

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def config(basepath, filename):
    fullpath = path.join(basepath, filename)
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s %(name)s %(asctime)s.%(msecs)03d %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(fullpath), logging.StreamHandler()
        ]
    )


def _get_time():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))


def info_time(text):
    logging.info(f"⧖ {text}")


def info(text):
    logging.info(f"→ {text}")


def start(text):
    start_time = time.time()
    logging.info(f"A {text}")
    return start_time


def end(start_time, text):
    elapsed_time = time.time() - start_time
    duration = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
    logging.info(f"Ω {text} Total: {duration}")


def logtime(decorated):
    def decorator(*args, **kw):
        start_time = start("Func:"+decorated.__name__)
        result = decorated(*args, **kw)
        end(start_time, "Func:"+decorated.__name__)
        return result
    return decorator
