class queue():	#큐 선언
    def __init__(self):
        self.arr = []
        
    def isEmpty(self):	#큐가 비어있는지 확인
        if self.arr == []:
            return True
        else:
            return False
        
    def enqueue(self, data):	#큐에 data 삽입
        self.arr.append(data)
        
    def dequeue(self):	#큐의 맨 앞 데이터 pop
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.arr.pop(0)
        
    def rear(self):	#큐의 맨 뒤 데이터 반환(pop 하지는 않음)
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.arr[-1]
        
    def front(self):	#큐의 맨 앞 데이터 반환(pop하지는 않음)
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.arr[0]
q = queue()
print(q.isEmpty())
q.enqueue(3)
q.enqueue(7)
q.enqueue(9)
q.enqueue(1)
q.enqueue(2)
print(q.front())
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.rear())
print(q.dequeue())