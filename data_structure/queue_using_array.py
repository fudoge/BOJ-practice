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
        
q = queue(4)	#[None, None, None, None]

print(q.isEmpty())	#True

q.enqueue(4)	#[4, None, None, None]
q.enqueue(7)	#[4, 7, None, None]
q.enqueue(2)	#[4, 7, 2, None]
q.enqueue(3)	#[4, 7, 2, 3]

print(q.isFull())	#True
q.enqueue(9)	#더 넣을 공간이 없음

print(q.dequeue())	#[None, 7, 2, 3]
print(q.dequeue())	#[None, None, 2, 3]
print(q.dequeue())	#[None, None, None, 3]
print(q.dequeue())	#[None, None, None, None]
print(q.isEmpty())
print(q.dequeue())	#큐는 비어있음

q.enqueue(8)	#분명 비어있는 큐인데.. 꽉 차있다??