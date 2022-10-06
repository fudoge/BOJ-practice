class Node():	#노드 선언
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Stack():	#스택 선언
    def __init__(self):
        self.head = None
        
    def isEmpty(self):	#스택이 비어있는지
        if self.head == None:
            return True
        else:
            return False
        
    def push(self,data):	#스택의 head에 값 추가
        if self.isEmpty():
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
            
    def pop(self):	#스택의 head제거
        if self.isEmpty():
            print("stack is Empty!")
        else:
            headNode = self.head
            self.head = self.head.next
            headNode.next = None
            return headNode.data
	
    def top(self):	#스택의 head값 출력
        if self.isEmpty():
            print("Stack is Empty!")
        else:
        	return self.head.data
    
s = Stack()
print(s.isEmpty())
s.push(7)
s.push(5)
s.push(3)
s.push(1)
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.top())
