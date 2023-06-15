from multiprocessing import Pool, current_process
from datetime import datetime
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize_solo(*number):
    result = []
    for num in number:
        res = []
        for i in range(1, num + 1):
            if num % i == 0:
                res.append(i)
        result.append(res)
    return result


def factorize_pool(*number):
    name = current_process().name
    logger.debug(f'{name} started...')
    result = []
    for num in number:
        res = []
        for i in range(1, num + 1):
            if num % i == 0:
                res.append(i)
        result.append(res)
    logger.debug(f'{name} ...stopped')
    return result[0]


def factorize(*numbers):
    with Pool(processes=2) as pool:
        result = pool.map(factorize_pool, numbers)
        logger.debug("All processes completed")
        return result


if __name__ == '__main__':
    start_time = datetime.now()
    a, b, c, d = factorize_solo(128, 255, 99999, 10651060)
    print(f"Time solo process: {datetime.now() - start_time}")

    start_time = datetime.now()
    e, f, g, h = factorize(128, 255, 99999, 10651060)
    print(f"Time multi process: {datetime.now() - start_time}")

    assert a == e == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == f == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == g == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == h == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
                      1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    logger.debug('End program')

