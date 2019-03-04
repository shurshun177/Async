from concurrent.futures import ThreadPoolExecutor
import threading
import multiprocessing
from functools import reduce
def task(b):
    print('Executing our Task')
    result = reduce(lambda x, y: x + y, range(10), b)
    print('I = {}'.format(result))
    print('Task Executed {}'.format(threading.current_thread()))

def main():
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        task1 = executor.submit(task, (20))
        task2 = executor.submit(task, (30))
        task3 = executor.submit(task,(40))
    print('All tasks complete')
main()