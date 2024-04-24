#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that will execute async_comprehension four
        times in parallel using asyncio.gather
    """
    begin = time()
    task = [async_comprehension() for i in range(4)]
    await gather(*task)
    end = time()
    return (end - begin)
