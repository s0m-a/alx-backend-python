#!/usr/bin/env python3
'''
    0. `The basics of async.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
