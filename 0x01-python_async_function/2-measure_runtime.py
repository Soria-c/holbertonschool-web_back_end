#!/usr/bin/env python3
"""async python"""

import asyncio
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures time execution"""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
