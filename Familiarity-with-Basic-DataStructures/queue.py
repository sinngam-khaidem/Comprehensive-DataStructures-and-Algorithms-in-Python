class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.contents = []
    
    def enqueue(self, val):
        if self.isFull():
            print("Queue is full")
            return
        self.size += 1
        self.contents.append(val)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        self.size -= 1
        return self.contents.pop(0)

    def get_size(self):
        return self.size

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0

def main():
    my_queue = Queue(5)
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print(my_queue.get_size())
    for i in range(my_queue.get_size()):
        print(my_queue.dequeue())
main()