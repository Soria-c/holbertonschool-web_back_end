#!/usr/bin/env python3
"""async python"""

import asyncio
from typing import Awaitable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """Task factory"""
    return asyncio.create_task(wait_random(max_delay))
