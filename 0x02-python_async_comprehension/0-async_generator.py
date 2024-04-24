#!/usr/bin/env python3

""" Async Comprehensions """

from random import uniform
from typing import Generator
from asyncio import sleep


async def async_generator() -> Generator[float, None, None]:
    """
      coroutine will loop 10 times, each time asynchronously
      wait 1 second,then yield a random number between 0 and 10
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
