#!/usr/bin/env python3
"""async python"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns results of task_wait_random"""
    r: List[float] = await asyncio\
        .gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(r)
