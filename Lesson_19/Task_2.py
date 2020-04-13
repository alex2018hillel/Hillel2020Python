import itertools
import pyzipper as pyzipper
import string, os, time
import threading
from queue import Queue

found = False

if not os.path.exists("dir"):
    with pyzipper.AESZipFile('lesson6.zip') as file:
        for item in itertools.permutations(string.ascii_lowercase, 3):
            word = (''.join(item))
            try:
                file.pwd = word.encode('ascii')
                file.extractall()
                print("Password is finding")
            except:
                pass

def worker_gen(q: Queue, num):
    print("Start worker: {}".format(num))
    global found
    with pyzipper.AESZipFile('lesson6.zip') as file:
        while True:
            if found:
                break
            password = q.get()
            if password is None:
                break
            print(password)
            try:

                file.extractall("dir", pwd=password)
                found = True
                print("Password is finding")
                break
            except:
                pass
    print("Finish generator {}".format(num))


def generator(q: Queue):
    print("Start")
    global found
    gen = itertools.permutations(string.ascii_lowercase, 3)
    max_q_size = 10
    for word in gen:
        if found:
            break
        while q.qsize() > max_q_size:
            time.sleep(0.0001)
            word = (''.join(word))
            word = word.encode('ascii')
            q.put(word)

    for i in range(n):
        q.put(None)
    print("Finish generator")

n = 20
q = Queue()
thread_g = threading.Thread(target=generator, args=(q, ))
workers = []
for iter in range(n):
    worker = threading.Thread(target=worker_gen, args=(q, iter))
    worker.start()
    workers.append(worker)

thread_g.start()
thread_g.join()
for worker in workers:
    worker.join()

if __name__ == "__main__":
    pass






# with pyzipper.AESZipFile('lesson6.zip') as file:
#         for item in itertools.permutations(string.ascii_lowercase, 3):
#             word = (''.join(item))
#             try:
#                 print(word)
#                 file.pwd = word.encode('ascii')
#                 file.extractall()
#                 print("Password is finding")
#             except:
#                 pass

