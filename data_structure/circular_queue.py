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
        
    def enqueue(self, data):	#큐에 data 삽입
        if self.last >= self.size or self.arr[self.last] != None:
            print("No space to enqueue!")
            return None
        self.arr[self.last] = data
        self.last = (self.last + 1)% self.size
        
    def dequeue(self):	#큐의 맨 앞 데이터 pop
        if self.isEmpty():
            return "Queue is Empty!"
        else:
            n = self.arr[self.first]
            self.arr[self.first] = None
            self.first = (self.first +1)% self.size
            return n
        
    def rear(self):	#큐의 맨 뒤 데이터 반환(pop하지는 않음)
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
print(q.arr)
q.enqueue(1)
print(q.arr)
q.enqueue(2)
print(q.arr)
print(q.front(), "1")
print(q.isEmpty(), "2")
print(q.dequeue(), "3")
print(q.dequeue(), "4")
print(q.front(), "5")
print(q.dequeue(), "6")
print(q.dequeue(), "7")
print(q.dequeue(), "8")
print(q.first)
print(q.last)
q.enqueue(4)
print(q.arr)
print(q.dequeue())
q.enqueue(9)
print(q.arr)
q.enqueue(1)
print(q.arr)
q.enqueue(2)
print(q.arr)
print(q.dequeue())
print(q.dequeue())
q.enqueue(7)
print(q.arr)