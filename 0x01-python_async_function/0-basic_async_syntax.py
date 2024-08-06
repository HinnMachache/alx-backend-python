#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
(max_delay,default value of 10) named wait_random that waits for
a random delay between 0 and max_delay (included & float value) & returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns max_delay: float
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
