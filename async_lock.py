import asyncio
import time
async def myWorker(lock):
    print('Attempting to attain lock')
    # acquire lock
    with await lock:
        # run critical section of code
        print('Currently locked')
        time.sleep(2)
    # our worker releases lock at this point
    print('Unlocked critical section')

async def main():
    # instantiate our lock
    lock = asyncio.Lock()
    # await the execution of 2 myWorker coroutines
    # each with our same lock instance passed in
    await asyncio.wait([myWorker(lock), myWorker(lock)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('All tasks completed')
loop.close()