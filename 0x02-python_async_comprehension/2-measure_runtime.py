#!/usr/bin/env python3
"""Python async"""

import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Computing runtime"""
    t0 = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - t0
