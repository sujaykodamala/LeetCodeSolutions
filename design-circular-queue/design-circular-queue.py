class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = 0
        self.maxsize = k
        self.head = 0
        self.tail = -1
        self.myqueue = [-1]*k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.tail = (self.tail+1) % self.maxsize
            self.size += 1
            self.myqueue[self.tail] = value
            return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.myqueue[self.head] = -1
            self.size -= 1
            self.head = (self.head+1) % self.maxsize
            return True
            

    def Front(self):
        """
        :rtype: int
        """
        return self.myqueue[self.head]


    def Rear(self):
        """
        :rtype: int
        """
        return self.myqueue[self.tail]

        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.maxsize:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()