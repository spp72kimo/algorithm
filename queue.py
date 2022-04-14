class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        print(f"{len(self.queue)} of index, insert '{data}'")
        self.queue.insert(len(self.queue), data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("佇列無資料")
            return
        else:
            print(f"Export {self.queue.pop(0)}")

    def showQueue(self):
        print("Show queue's data:")
        for d in self.queue:
            print(d)


Q = Queue()
Q.enqueue("apple")
Q.enqueue("banana")
Q.showQueue()
Q.dequeue()
Q.showQueue()
