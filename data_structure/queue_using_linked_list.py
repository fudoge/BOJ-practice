class Node():	#노드 선언
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class queue():	#스택 선언
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):	#스택이 비어있는지
        if self.head == None and self.tail == None:
            return True
        else:
            return False

    def enqueue(self, data): #tail에 추가, 빈 리스트일경우, head에.
        if self.isEmpty():
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            
    def dequeue(self):	#스택의 head제거
        if self.isEmpty():
            print("stack is Empty!")
        else:
            data = self.head.data
            headNode = self.head
            self.head = self.head.next
            headNode.next = None
            return data
	
    def front(self):	#큐의 head값 출력
        if self.isEmpty():
            print("Stack is Empty!")
        else:
        	return self.head.data
    def rear(self):		#큐의 끝값 출력
        if self.isEmpty():
            print("Stack is Empty!")
        else:
        	return self.tail.data
        
        
q = queue()
print(q.isEmpty())
q.enqueue(3)
q.enqueue(7)
q.enqueue(1)
q.enqueue(8)
q.enqueue(2)
print(q.isEmpty())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.rear())
print(q.dequeue())
