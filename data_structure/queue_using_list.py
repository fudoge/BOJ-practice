class queue():
    def __init__(self):
        self.arr = []
    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False
    def enqueue(self, data):
        self.arr.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            return self.arr.pop(0)
    def rear(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            return self.arr[-1]
    def front(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            return self.arr[0]
q = queue()
print(q.isEmpty())
q.enqueue(3)
q.enqueue(7)
q.enqueue(9)
q.enqueue(1)
q.enqueue(2)
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.rear())
print(q.dequeue())