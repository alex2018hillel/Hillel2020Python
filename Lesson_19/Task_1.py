import asyncio
import datetime


async def is_prime(num):
    if num <= 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5 + 1)):
        await asyncio.sleep(0)
        if num % i == 0:
            return False
    return True


max_running = 20
sem = asyncio.Semaphore(max_running)
new_list = []

async def call_is_prime(n):
    async with sem:
        p = await is_prime(n)
        if p:
            new_list.append(p)

loop = asyncio.get_event_loop()

start = datetime.datetime.now()
fut = asyncio.gather(*[call_is_prime(p) for p in range(1_000_000)])
finish = datetime.datetime.now()
print(len(new_list))
print('futures list: ', finish - start)

start = datetime.datetime.now()
loop.run_until_complete(fut)
finish = datetime.datetime.now()
print(len(new_list))
print('primes finished: ', finish - start)

