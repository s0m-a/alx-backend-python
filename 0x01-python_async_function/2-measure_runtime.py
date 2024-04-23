#!/usr/bin/env python3

from asyncio import run
from time import time

""" 2. Measure the runtime """

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time"""
    begin = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - begin) / n
