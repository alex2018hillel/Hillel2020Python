import datetime, sys, time

def itime():
    return str(datetime.datetime.now())

def switcher(*tasks):
    taskqueue = [task() for task in tasks]    # Start all generators
    while taskqueue:                          # While any running tasks remain
        front = taskqueue.pop(0)              # Fetch next task at front
        try:
            result = next(front)              # Resume task, run to its next yield
        except StopIteration:
            pass                              # Returned: task finished
        else:
            name = front.__name__             # Yielded: reschedule at end of queue
            print(name, result, itime())
            taskqueue.append(front)


def task1():
    for i in range(6):       # Resumed here by next() in switcher (or for)
        time.sleep(0.1)       # Simulate a nonpreemptable action here
        yield i             # Suspend and yield control back to switcher (or for)
                            # Removed from queue on return (or exit for)
def task2():
    for i in range(3):
        time.sleep(0.2)
        yield i

def task3():
    for i in range(2):
        time.sleep(0.3)
        yield i


if __name__ == '__main__':
    #
    # SERIAL: with command-line arg, run the functions by themselves.
    # Each task checks in at regular intervals and runs atomically.
    #
    print('SERIAL')
    start = datetime.datetime.now()
    for i in task1(): print('task1', i, itime())
    for i in task2(): print('task2', i, itime())
    for i in task3(): print('task3', i, itime())
    print('all tasks finished, total time: {}'.format(
        datetime.datetime.now() - start))

    #
    # ASYNCHRONOUS: without arg, run the functions together, overlapped.
    # Tasks check in at irregular intervals and run interleaved.
    #
    print('ASYNCHRONOUS')
    start = datetime.datetime.now()
    switcher(task1, task2, task3)
    print('all tasks finished, total time: {}'.format(
        datetime.datetime.now() - start))