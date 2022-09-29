class Node():	#노드 선언
	def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        
    def pop():
        if self.isEmpty():
            print("stack is Empty!")
        else:
            headNode = self.head
        	self.head = self.head.next
        	headNode.next = None
        	return headNode
        
    def top():
        return self.head
    
