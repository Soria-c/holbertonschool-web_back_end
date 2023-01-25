#!/usr/bin/env python3
"""Python async"""

import asyncio
import random


async def async_generator():
    """Async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
