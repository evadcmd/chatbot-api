import asyncio

import pytest


async def add_async(x: int, y: int):
    await asyncio.sleep(0.5)
    return x + y


@pytest.mark.asyncio
async def test_add_async():
    sum = await add_async(2, 3)
    assert sum == 2 + 3
