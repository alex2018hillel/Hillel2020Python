def simple_zip(*tasks):
    taskqueue = [task() for task in tasks]
    l = []
    tup = []
    i = 1
    while taskqueue:
        front = taskqueue.pop(0)
        try:
            result = next(front)
        except StopIteration:
            result = None
        else:
            taskqueue.append(front)
        if result != None:
            if (i<=len(tasks)) and result != None:
                tup.append(result)
                i += 1
            else:
                l.append(tuple(tup))
                tup = [result]
                i = 2
        else: break
    return (l)

def first_arg():
    for i_t in t:
        yield (i_t)

def second_arg():
    for i_s in s:
        yield (i_s)

if __name__ == '__main__':
    t = tuple(range(1,9))
    s = 'ABCD'
    print(simple_zip(first_arg, second_arg))
