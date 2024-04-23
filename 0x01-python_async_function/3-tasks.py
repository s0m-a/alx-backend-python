#!/usr/bin/env python3

from asyncio import Task, create_task
""" 3. Task """
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ create's tasks """
    tasks = create_task(wait_random(max_delay))
    return tasks
