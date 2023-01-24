#!/usr/bin/env python3
"""async python"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Returns the total wait time"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns results of wait_random"""
    r: List[float] = await asyncio\
        .gather(*(wait_random(max_delay) for i in range(n)))
    r.sort()
    return r
