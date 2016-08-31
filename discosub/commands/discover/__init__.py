import argparse
import sys
import os
import socket
import datetime
import time
import threading
try:
    import Queue
except ImportError:
    import queue as Queue
from discosub.core.ui import info, success, fail

results = []

def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


class Tester(threading.Thread):

    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self._queue = queue
        self.name = name

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._queue.get()

            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            try:
                print("testing: {0}".format(msg))
                ip = socket.gethostbyname(msg)
                result = '{0} => {1}'.format(msg, ip)
                results.append(result)
            except socket.gaierror:
                continue


def thats_all_folks(start):
    end = datetime.datetime.now()
    hours, minutes, seconds = convert_timedelta(end - start)
    print("Ending at {0}\n".format(end))
    print("{0} results find in {1} hours {2} minutes {3} seconds".format(
        len(results), hours, minutes, seconds))
    print("Results:")
    for result in results:
        print(result)


def analyze(args):
    start = datetime.datetime.now()
    subdomains = []
    with open(os.path.join("dictionaries", "default.txt")) as myDictionary:
        subdomains = myDictionary.readlines()

    print("We have {0} possibilities".format(len(subdomains)))
    print("Starting at {0}\n".format(start))

    queue = Queue.Queue()
    workers = []
    for index in range(0, 1000):
        worker = Tester(queue, "worker{0}".format(index))
        worker.start()
        workers.append(worker)

    [queue.put("{0}.{1}".format(sub.replace("\n", ""), args.target)) for sub in subdomains]
    [queue.put("quit") for worker in workers]

    for worker in workers:
        worker.join()

    thats_all_folks(start)

def discover():
    global VERBOSE
    parser = argparse.ArgumentParser(
    description='Run a subdomain scanner on specified target')
    parser.add_argument('target', help='The root specified domain')
    parser.add_argument('--verbose', help='Activate the verbose mode',
        default="no")
    args = parser.parse_args(sys.argv[2:])
    analyze(args)