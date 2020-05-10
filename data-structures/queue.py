# Must Read Blog: https://dbader.org/blog/queues-in-python
# The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time.
# Python’s deque objects are implemented as doubly-linked lists which gives them excellent performance for enqueuing and dequeuing 
# elements, but poor O(n) performance for randomly accessing elements in the middle of the queue.
# Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.
# collections.deque is a great default choice if you’re looking for a queue data structure in Python’s standard library.
from collections import deque

class Queue:
    def __init__(self, items):
        self.items = deque(items)
    
    def enqueue(self, item):
        """
        insert element into queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        delete element from queue
        """
        self.items.popleft()
    
    def size(self):
        """
        return the total size queue
        """
        return len(self.items)
    
    def isEmpty(self):
        """
        Queue is empty or not
        """
        return len(self.items) == 0

def main():
    #  Stack Operation
    q=Queue(["1","2"])
    q.enqueue("3")
    q.dequeue()
    print("Size of queue", q.size())
    print(q.items)
    print("Queue is empty or not: ", q.isEmpty())


if __name__ == "__main__":
    main()