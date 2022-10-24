class circular_queue():	#큐 선언
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.first = 0
        self.last = 0
        
    def isEmpty(self):	#큐가 비어있는지 확인
        if self.first == self.last and self.arr[self.first] == None:
            return True
        else:
            return False

    def isFull(self):	#큐가 꽉 차있는지 확인
        if self.first == self.last and self.arr[self.first] != None:
            return True
        else:
            return False
        
    def enqueue(self, data):	#큐에 data 삽입
        if self.isFull():
            print("Queue is Full!")
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
            return("Queue is Empty!")
        else:
            return self.arr[self.last]
        
    def front(self):	#큐의 맨 앞 데이터 반환(pop하지는 않음)
        if self.isEmpty():
            return("Queue is Empty!")
        else:
            return self.arr[self.first]
        
q = circular_queue(4)

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
print(q.isEmpty())	#True
print(q.dequeue())	#더 뺄게 없음

q.enqueue(8)		#[8, None, None, None]
print(q.dequeue())	#[None, None, None, None]
q.enqueue(9)		#[None, 9, None, None]
q.enqueue(1)		#[None, 9, 1, None]
q.enqueue(6)		#[None, 9, 1, 6]
q.enqueue(4)		#[4, 9, 1, 6]
print(q.arr)		#[4, 9, 1, 6]
print(q.front())	#9
