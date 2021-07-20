from random import SystemRandom
import requests, time, threading, queue, copy

def multithreading(dataList, func, NUM_THREAD=10):
    exitFlag = 0
    start_time = time.time()

    class MultiThread (threading.Thread):
        def __init__(self, threadID, name, q, func):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
            self.func = copy.deepcopy(func)
        def run(self):
            print ("[+] Starting " + self.name)
            process_data(self.name, self.q, self.func)
            print ("[-] Exiting " + self.name)

    
    def process_data(threadName, q, func):
        while not exitFlag:
            if not workQueue.empty():
                data = q.get()
                func(*data)
                print ("[+] %s processing %s" % (threadName, data))
            else:
                time.sleep(1)

    threadList = ["Thread-" + str(i+1) for i in range(NUM_THREAD)]
    # queueLock = threading.Lock()
    workQueue = queue.Queue()
    threads = []
    threadID = 1

    # Create new threads
    for tName in threadList:
        thread = MultiThread(threadID, tName, workQueue, func)
        thread.start()
        threads.append(thread)
        threadID += 1

    # Fill the queue
    # queueLock.acquire()
    for data in dataList:
        workQueue.put(data)
    # queueLock.release()

    # Wait for queue to empty
    while not workQueue.empty():
        pass

    # Notify threads it's time to exit
    exitFlag = 1

    # Wait for all threads to complete
    for t in threads:
        t.join()

    total_time = (time.time() - start_time)
    print("[*] Total time: %s seconds" % str(total_time))
    print("[!] Exiting Main Thread")


if __name__ == '__main__':
    # TODO
    pass