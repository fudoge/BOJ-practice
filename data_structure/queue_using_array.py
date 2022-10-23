class queue():	#큐 선언
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.first = 0
        self.last = 0
        
    def isEmpty(self):	#큐가 비어있는지 확인
        if self.first >= self.size:
            return True
        if self.arr[self.first] == None:
            return True
        else:
            return False
        
    def isFull(self):	#큐가 꽉 차있는지 확인
        return self.last == self.size
        
    def enqueue(self, data):	#큐에 data 삽입
        if self.isFull() is True:
            print("Queue is Full!")
            return None
        self.arr[self.last] = data
        self.last = self.last + 1
        
    def dequeue(self):	#큐의 맨 앞 데이터 pop
        if self.isEmpty():
            return "Queue is Empty!"
        else:
            n = self.arr[self.first]
            self.arr[self.first] = None
            self.first = self.first +1
            return n
        
    def rear(self):	#큐의 맨 뒤 데이터 반환(pop 하지는 않음)
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.arr[self.last]
        
    def front(self):	#큐의 맨 앞 데이터 반환(pop하지는 않음)
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.arr[self.first]
        
q = queue(4)
print(q.isEmpty())
q.enqueue(3)
print(q.arr)
q.enqueue(7)
print(q.arr)
q.enqueue(9)
q.enqueue(1)
print(q.arr)
print(q.isFull(), "0")
q.enqueue(2)
print(q.front(), "1")
print(q.isEmpty(), "2")
print(q.dequeue(), "3")
print(q.dequeue(), "4")
print(q.front(), "5")
print(q.dequeue(), "6")
print(q.dequeue(), "7")
print(q.dequeue(), "8")
q.enqueue(4)