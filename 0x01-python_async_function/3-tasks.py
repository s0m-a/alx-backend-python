#!/usr/bin/env python3

from asyncio import Task, create_task
""" 3. Task """
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ A function that task_wait_random that takes
    an integer max_delay and returns a asyncio
    """
    tasks = create_task(wait_random(max_delay))
    return tasks
