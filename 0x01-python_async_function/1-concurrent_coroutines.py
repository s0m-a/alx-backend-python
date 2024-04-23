#!/usr/bin/env python3

import asyncio
from typing import List

""" The basics of async """

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Will spawn wait_random n times with the specified max_delay,
    list of the delays should be in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
